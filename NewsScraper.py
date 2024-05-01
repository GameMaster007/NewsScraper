import asyncio
import aiohttp
import feedparser
import sys
import logging
from typing import List, Dict

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_rss_feed_async(session: aiohttp.ClientSession, url: str) -> List[Dict[str, str]]:
    """
    Asynchronously fetches and parses an RSS feed from the given URL.
    Returns a list of dictionaries containing the title and link of each entry.
    """
    try:
        async with session.get(url) as response:
            if response.status == 200:
                feed = feedparser.parse(await response.text())
                return [{"title": entry.title, "link": entry.link} for entry in feed.entries]
            else:
                logging.error(f"Failed to fetch the RSS feed from {url}. Status code: {response.status}")
                return []
    except Exception as e:
        logging.error(f"An error occurred while fetching the RSS feed from {url}: {e}")
        return []

async def print_feed_entries_async(entries: List[Dict[str, str]]) -> None:
    """
    Asynchronously prints the title and link of each entry in the provided list.
    """
    for entry in entries:
        print(f"Title: {entry['title']}")
        print(f"Link: {entry['link']}\n")

def filter_entries_by_keyword(entries: List[Dict[str, str]], keyword: str) -> List[Dict[str, str]]:
    """
    Filters the list of entries to include only those that contain the keyword in their title or link.
    """
    return [entry for entry in entries if keyword.lower() in entry['title'].lower() or keyword.lower() in entry['link'].lower()]

async def main():
    """
    Main function to fetch and print RSS feeds asynchronously.
    Optionally filters entries by a keyword.
    """
    urls = [
        "http://feeds.abcnews.com/abcnews/usheadlines",
        "http://rss.cnn.com/rss/cnn_topstories.rss"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_rss_feed_async(session, url) for url in urls]
        entries_list = await asyncio.gather(*tasks)
        for entries in entries_list:
            if keyword:
                filtered_entries = filter_entries_by_keyword(entries, keyword)
                await print_feed_entries_async(filtered_entries)
            else:
                await print_feed_entries_async(entries)

if __name__ == "__main__":
    try:
        keyword = input("Enter a keyword to search for in the news: ")
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Interrupted by user. Exiting...")
        sys.exit(0)