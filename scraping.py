import csv
from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
get_data = requests.get(url)

if get_data.status_code == 200:
    soup = BeautifulSoup(get_data.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Author', 'Quote'])  # Write header

        for quote, author in zip(quotes, authors):
            csv_writer.writerow([author.get_text(), quote.get_text()])  # Write each quote and author
else:
    print(f"Failed to retrieve data. Status code: {get_data.status_code}")
