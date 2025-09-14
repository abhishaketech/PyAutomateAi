import requests  # for sending HTTP requests 
from bs4 import BeautifulSoup  # to parse and extract data from HTML content
import csv

def scrape_books(url="https://www.bookswagon.com/promo-best-seller/box-sets/389DA2389287"):

    '''1. Send a GET request to the URL
    2. Parse the HTML content using BeautifulSoup
    3. Find all book elements using their HTML tag and class
    4. Extract title and price for each book
    5. Store the data in a list of dictionaries
    6. Return the scraped data'''
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    scraped_data = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        scraped_data.append({"title": title, "price": price})

    return scraped_data

def save_to_csv(data, filename="books1.csv"):

    '''1. Open the CSV file in write mode
    2. Use DictWriter to write headers and rows
    3. Save title and price fields'''

    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price"])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    data = scrape_books()
    save_to_csv(data)
    print(f"Scraped and saved {len(data)} books to books.csv")

'''Currently for demo, a books website is used. 
After checking the terms of usage of any website, we can send HTTP requests to that website
and parse the data from there too using the parser from beautifulsoup'''
