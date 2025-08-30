"""
SCRAPINGAI - Basic Scraper Example

This example demonstrates how to use the ScrapingAI library for basic web scraping tasks.
"""

import sys
import os

# Add the parent directory to the path so we can import the ScrapingAI module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraping_tools import ScrapingAI

def main():
    """Run a basic web scraping example."""
    print("SCRAPINGAI - Basic Scraper Example")
    print("----------------------------------")
    
    # Initialize the scraper
    scraper = ScrapingAI()
    
    # Define the URL to scrape
    url = "https://news.ycombinator.com/"
    print(f"Scraping: {url}")
    
    # Fetch and parse the page
    html = scraper.fetch_page(url)
    soup = scraper.parse_html(html)
    
    # Extract story titles
    story_titles = scraper.extract_text(soup, ".titleline > a")
    
    # Extract story points
    story_points = scraper.extract_text(soup, ".score")
    
    # Print the results
    print(f"\nFound {len(story_titles)} stories:")
    for i, (title, points) in enumerate(zip(story_titles, story_points), 1):
        print(f"{i}. {title} ({points})")
    
    # Extract all links
    links = scraper.extract_links(soup, base_url=url)
    print(f"\nFound {len(links)} links on the page")
    
if __name__ == "__main__":
    main()