import requests
from bs4 import BeautifulSoup
import sqlite3

def crawler(start_url, max_pages=100):
    
    connection = sqlite3.connect('crawled_pages.db')
    cursor = connection.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS pages (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       url TEXT UNIQUE,
                       content TEXT
                   )
                   ''')
    connection.commit()
    
    url_frontier = [start_url]
    visited_pages = set()
    
    while url_frontier and len(visited_pages) < max_pages:
        url = url_frontier.pop(0)
        if url in visited_pages:
            continue

        print(f"Crawling {url}")
        response = requests.get(url)
    
        if response.status_code != 200:
            continue    

        soup = BeautifulSoup(response.content, "html.parser")

        connection.execute('INSERT OR IGNORE INTO pages (url,content) VALUES (?,?)', (url, str(soup)))
        connection.commit()
        
        links = soup.find_all("a")

        for link in links:
            href = link.get("href")
            if href and "http" in href and href not in visited_pages:
                url_frontier.append(href)

        visited_pages.add(url)
    
    connection.close()

seed_urls = ["https://kenh14.vn/star.chn"]

for url in seed_urls:
    crawler(url,50)