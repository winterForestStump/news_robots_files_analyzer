from datetime import date
import requests
import pandas as pd
from tqdm import tqdm
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

month_folder = 'march_2025'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
today = str(date.today())

def main():
    df = pd.read_csv(f'data/{month_folder}/news_best_100.csv')
    for i in tqdm(range(len(df))):
        try:
            url = f"https://www.{df['Website'].iloc[i]}/robots.txt"
            response = requests.get(url, headers=headers)
            if response.status_code != 200: #check if the response from the URL is not successful (other status code than 200)
                print(f"Error: Failed to retrieve page for url {url}. Status code: {response.status_code}")
                continue
            texts = response.text
            df.at[i, 'robots'] = texts
        except ConnectionError as e:
            print(f"ConnectionError occurred: {e}")
            continue
        except Timeout:
            print("Request timed out. Retrying...")
            continue
        except TooManyRedirects:
            print("Too many redirects. Check the URL or handle redirects manually.")
            continue
        except TooManyRedirects:
            print(f"An unexpected error occurred: {e}")
            continue

    df.to_csv(f'data/{month_folder}/robots_txt_{today}_agents.csv')


if __name__ == "__main__":
    main()