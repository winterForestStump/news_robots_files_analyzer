import requests
from bs4 import BeautifulSoup
import csv

month_folder = 'march_2026'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
url = 'https://ahrefs.com/websites/news'

def main():
    response = requests.get(url)
    if response.status_code != 200: #check if the response from the URL is not successful (other status code than 200)
        print(f"Error: Failed to retrieve page for url {url}. Status code: {response.status_code}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    #table = soup.find("table", class_="css-e8l0hj-table")
    #//*[@id="websites-table"]/tbody
    table = soup.find("table", id="websites-table")
    #table = table.select_one('tbody')
    headers = [header.text.strip() for header in table.find_all("th")]
    rows = []
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        if cells:
            row_data = []
            for cell in cells:
                cell_text = ' '.join(cell.text.strip().split())
                row_data.append(cell_text)
            rows.append(row_data)
    # Save to CSV
    with open(f"data/{month_folder}/news_best_100.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers
        writer.writerows(rows)  # Write rows

    print(f"Data saved to data/{month_folder}/news_best_100.csv")

if __name__ == '__main__':
    main()