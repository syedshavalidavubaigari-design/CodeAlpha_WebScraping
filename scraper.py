
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Public practice website for web scraping
url = "https://books.toscrape.com/"

print("Starting CodeAlpha Web Scraping Project...")

try:
    response = requests.get(url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    df = pd.DataFrame(books)
    df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")

    print("\nScraping completed successfully!")
    print("Total books collected:", len(df))
    print("\nFirst five records:")
    print(df.head().to_string(index=False))
    print("\nSaved file: books_data.csv")

except requests.RequestException as error:
    print("Website connection failed:", error)
