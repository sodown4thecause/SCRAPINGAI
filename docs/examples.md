# Examples

This page provides examples of how to use SCRAPINGAI for various web scraping tasks.

## Basic Usage

Here's a simple example of how to use SCRAPINGAI to scrape a web page:

```python
from scraping_tools import ScrapingAI

# Initialize the scraper
scraper = ScrapingAI()

# Fetch and parse a web page
html = scraper.fetch_page("https://example.com")
soup = scraper.parse_html(html)

# Extract content using CSS selectors
headings = scraper.extract_text(soup, "h1, h2, h3")
links = scraper.extract_links(soup)

# Print results
print(f"Found {len(headings)} headings:")
for heading in headings:
    print(f"- {heading}")
```

## Scraping News Headlines

This example shows how to scrape news headlines from Hacker News:

```python
from scraping_tools import ScrapingAI

def scrape_hacker_news():
    """Scrape top stories from Hacker News."""
    print("SCRAPINGAI - Hacker News Scraper Example")
    print("---------------------------------------")
    
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
    
if __name__ == "__main__":
    scrape_hacker_news()
```

## Scraping Multiple Pages

This example demonstrates how to scrape multiple pages with a delay between requests:

```python
from scraping_tools import ScrapingAI

def scrape_multiple_pages():
    """Scrape content from multiple pages."""
    # Initialize the scraper
    scraper = ScrapingAI()
    
    # List of URLs to scrape
    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]
    
    # Scrape all URLs with a delay between requests
    # Extract all paragraph text from each page
    results = scraper.scrape_with_delay(urls, "p", delay_range=(2, 5))
    
    # Process the results
    for url, paragraphs in results.items():
        print(f"\nContent from {url}:")
        for i, paragraph in enumerate(paragraphs, 1):
            print(f"{i}. {paragraph[:100]}...")  # Print first 100 chars of each paragraph
    
if __name__ == "__main__":
    scrape_multiple_pages()
```

## Extracting Specific Content

This example shows how to extract specific content using CSS selectors:

```python
from scraping_tools import ScrapingAI

def extract_specific_content():
    """Extract specific content from a web page."""
    # Initialize the scraper
    scraper = ScrapingAI()
    
    # Fetch and parse the page
    url = "https://quotes.toscrape.com/"
    html = scraper.fetch_page(url)
    soup = scraper.parse_html(html)
    
    # Extract quotes
    quotes = scraper.extract_text(soup, ".quote .text")
    
    # Extract authors
    authors = scraper.extract_text(soup, ".quote .author")
    
    # Extract tags (this is more complex, so we'll use BeautifulSoup directly)
    tag_lists = []
    for quote_div in soup.select(".quote"):
        tags = [tag.get_text() for tag in quote_div.select(".tags .tag")]
        tag_lists.append(tags)
    
    # Print the results
    print(f"Found {len(quotes)} quotes:")
    for i, (quote, author, tags) in enumerate(zip(quotes, authors, tag_lists), 1):
        print(f"{i}. {quote}")
        print(f"   - By: {author}")
        print(f"   - Tags: {', '.join(tags)}")
        print()
    
if __name__ == "__main__":
    extract_specific_content()
```