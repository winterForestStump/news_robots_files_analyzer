import argparse
import pandas as pd
import cohere
import os
from dotenv import load_dotenv
from tqdm import tqdm
import time
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
load_dotenv()

COHERE_API = os.getenv('COHERE_API_KEY')
cohere_client = cohere.ClientV2(api_key=COHERE_API)

def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file-name", dest="file_name", help="Name of the file", required=True)
    return parser.parse_args()

def main():
    args = parse_cli_args()
    df = pd.read_csv(f"data/{str(args.file_name)}")
    system_message = '''
        You are a text analyst. You will be provided with text data from robots.txt files of the nes websites. 
        Your task is to find in the text the names of LLM's agents (e.g. GPT, Claude and etc).
        Provide only the names, without any additional information.
        '''
    for i in tqdm(range(len(df))):
        try:
            robot_text = df['robots'][i]
            response = cohere_client.chat(model="command-r-plus-08-2024", 
                                        messages=[{"role": "system", "content": system_message},
                                                    {"role": "user", "content": f"Text from the robots.txt file: {robot_text}",},
                                                ],
                                        temperature = 0.1,
                                        )

            res = response.message.content[0].text.split('\n')
            final_response = '\n'.join(res)
            df.at[i, 'agents'] = final_response
            time.sleep(5)
            
        except ConnectionError as e:
            print(f"ConnectionError occurred: {e}")
            continue
        except Timeout:
            print("Request timed out. Retrying...")
            continue
        except TooManyRedirects:
            print("Too many redirects. Check the URL or handle redirects manually.")
            continue

    df.to_csv(f"data/{str(args.file_name)}_agents")
    print('Success. File saved')

if __name__ == "__main__":
    main()