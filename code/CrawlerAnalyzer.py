# this script runs news websites' robots.txt crawler, analyses the disallowed bots and agents, and provide a readme report
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
from datetime import date
from tqdm import tqdm
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
url = 'https://ahrefs.com/websites/news'

def crawle_news():
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Failed to retrieve page for url {url}. Status code: {response.status_code}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find("span", class_="text-[var(--color-text-secondary)] text-[length:var(--font-size-body)] leading-[var(--line-height-body)]")
    folder_name = date.text.strip().replace(' ','_')
    Path("../data", folder_name).mkdir(parents=True, exist_ok=True)
    table = soup.find("table", id="websites-table")
    headers = [header.text.strip() for header in table.find_all("th")]
    headers = [header.text for header in table.find_all("th")]
    result = []
    for item in headers:
        if item:
            parts = item.split('\n\n')
            for part in parts:
                if part.strip():
                    result.append(part.strip())
    rows = []
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if cells:
            row_data = []
            for cell in cells[:1] + cells[2:]:  # take all except index 1
                cell_text = ' '.join(cell.text.strip().split())
                row_data.append(cell_text)
            rows.append(row_data)

    dataframe = pd.DataFrame(rows, columns=result)
    dataframe.drop(columns = ['Rank by estimated organic search traffic'], inplace=True)
    dataframe['Search traffic'] = [dataframe['Search traffic'][i].split()[0] for i in range(len(dataframe))]
    dataframe.to_csv(f"data/{folder_name}/news_best_100.csv")
    return dataframe, folder_name


def crawle_robots_txt(dataframe, folder_name):
    for i in tqdm(range(len(dataframe))):
        try:
            url = f"https://www.{dataframe['Website'].iloc[i]}/robots.txt"
            response = requests.get(url, headers=headers)
            if response.status_code != 200: 
                print(f"Error: Failed to retrieve page for url {url}. Status code: {response.status_code}")
                continue
            texts = response.text
            dataframe.at[i, 'robots'] = texts
        except ConnectionError as e:
            print(f"ConnectionError  for {url}: {e}")
            continue
        except Timeout:
            print(f"Request timed out for {url}. Retrying...")
            continue
        except TooManyRedirects:
            print(f"Too many redirects for {url}. Check the URL or handle redirects manually.")
            continue
        except TooManyRedirects as e:
            print(f"An unexpected error occurred for {url}: {e}")
            continue
    dataframe.to_csv(f'data/{folder_name}/robots_txt_agents.csv')
    return dataframe

def analyze_robots_txt(dataframe, folder_name):
    output_path = Path(f"data/{folder_name}")
    output_file = output_path / "disallowed_bots.csv"

    robots_texts = dataframe

    results = []
    today = str(date.today())

    for _, row in tqdm(robots_texts.iterrows(), total=len(robots_texts)):
        website = row['Website']
        robots_text = row['robots']

        # Skip if robots_text is not a string
        if not isinstance(robots_text, str):
            continue
        
        bots = []
        lines = robots_text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith('User-agent:'):
                bot = line.split('User-agent:')[1].strip()
                # Check next line for Disallow: /
                if i+1 < len(lines) and lines[i+1].strip() == 'Disallow: /':
                    bots.append(bot)
        
        if bots:  # Only add rows with found bots
            for bot in bots:
                results.append({
                    'Date': today,
                    'Website': website,
                    'Disallowed Bot': bot
                })
    
    # Create and save DataFrame
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    return df

def analyze_txt_and_create_readme(df, folder_name):
    list_ai = pd.read_table('list/list_ai.txt', header = None)
    list_file_length = len(list_ai)

    df['ai'] = int(0)
    for _, i in enumerate(df['Disallowed Bot']):
        if i in list(list_ai[0]):
            df.at[_, 'ai'] = int(1)

    # Total unique websites
    total_websites = df['Website'].nunique()

    # Websites with at least one AI bot disallowed
    websites_with_ai = df[df['ai'] == 1]['Website'].nunique()

    # Percentage
    percentage = websites_with_ai / total_websites

    # Top 5 Disallowed AI Bots
    top_ai_bots = pd.DataFrame(df[df['ai'] == 1]['Disallowed Bot'].value_counts().head(5))
    top_ai_bots_df = top_ai_bots.reset_index()
    top_ai_bots_df.columns = ['Disallowed Bot', 'Count']
    top_ai_bots_md = top_ai_bots_df.to_markdown(index=False)

    # Top 5 Websites by AI Bot Disallowances
    top_websites_ai = pd.DataFrame(df[df['ai'] == 1]['Website'].value_counts().head(5))
    top_websites_ai_df = top_websites_ai.reset_index()
    top_websites_ai_df.columns = ['Website', 'Count']
    top_websites_ai_md = top_websites_ai_df.to_markdown(index=False)


    total_bots = len(df)
    ai_bots = df['ai'].sum()
    ai_share = ai_bots / total_bots * 100

    # Read template
    with open('template/template.md', 'r') as f:
        content = f.read()

    # Replace placeholders
    content = content.replace('{{percentage}}', f"{(percentage) * 100:.0f}%")
    content = content.replace('{{top_ai_bots_md}}', top_ai_bots_md)
    content = content.replace('{{top_websites_ai_md}}', top_websites_ai_md)
    content = content.replace('{{ai_share}}', f"{(ai_share):.0f}%")
    content = content.replace('{{total_websites}}', str(total_websites))
    content = content.replace('{{websites_with_ai}}', str(websites_with_ai))
    content = content.replace('{{total_bots}}', str(total_bots))
    content = content.replace('{{ai_bots}}', str(ai_bots))
    content = content.replace('{{folder_name}}', folder_name)
    content = content.replace('{{list_file_length}}', str(list_file_length))

    # Write final output
    with open('readme.md', 'w') as f:
        f.write(content)

def main():
    dataframe, folder_name = crawle_news()
    dataframe = crawle_robots_txt(dataframe, folder_name)
    df = analyze_robots_txt(dataframe, folder_name)
    analyze_txt_and_create_readme(df, folder_name)

if __name__ == '__main__':
    main()