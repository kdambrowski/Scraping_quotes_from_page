import requests
import json
import unicodedata
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import time


def find_env_file(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".env"):
            return os.path.join(folder, filename)
    return None


def normalize_text(text):
    normalized_text = unicodedata.normalize('NFKD', text)
    return normalized_text.replace('“', "'").replace('”', "'")


def scrape_quotes(url, output_file):
    load_dotenv(find_env_file(os.getcwd()))
    page_num = 1

    while True:
        response = requests.get(url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        target_script = None
        for script in soup.find_all('script'):
            if 'text' in script.text:
                target_script = script.text
                break

        if target_script is None:
            break

        start_index = target_script.find('[')
        end_index = target_script.find('];') + 1
        quotes_data = target_script[start_index:end_index]

        try:
            quotes = json.loads(quotes_data)
            for quote in quotes:
                quote['text'] = normalize_text(quote['text'])

        except json.JSONDecodeError as e:
            print("JSON parse invalid:", e)

        with open(output_file, "a", encoding='utf-8') as file:
            for quote in quotes:
                quote_data = {
                    "text": quote['text'],
                    "by": quote['author']['name'],
                    "tags": quote['tags']
                }
                json.dump(quote_data, file, ensure_ascii=False, indent=2)
                file.write("\n")

        next_page = soup.find('li', class_='next')
        if not next_page:
            break
        url = next_page.find('a')['href']
        url = f'http://quotes.toscrape.com{url}'
        page_num += 1
        time.sleep(2)

    print(f"Quotes from {page_num} pages have been saved in the output file.")


load_dotenv(find_env_file(os.getcwd()))
input_url = os.getenv("INPUT_URL")
output_file = os.getenv("OUTPUT_FILE")