# Quick Start Guide

This guide will help you get started with SCRAPINGAI quickly.

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

## Extracting Specific Content

You can use CSS selectors to extract specific content from web pages:

```python
# Extract all paragraph text
paragraphs = scraper.extract_text(soup, "p")

# Extract all links from a specific section
nav_links = scraper.extract_text(soup, "nav a")

# Extract all image sources
images = [img["src"] for img in soup.select("img")]
```

## Handling Multiple Pages

SCRAPINGAI provides tools for scraping multiple pages with built-in delays to be respectful:

```python
# List of URLs to scrape
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

# Scrape all URLs with a delay between requests
results = scraper.scrape_with_delay(urls, "h1", delay_range=(2, 5))

# Process the results
for url, content in results.items():
    print(f"Content from {url}:")
    for item in content:
        print(f"- {item}")
```

## Next Steps

- Check out the [API Reference](api-reference.md) for detailed information about all available methods
- See the [Examples](examples.md) for more complex usage scenarios
- Learn about [Advanced Features](advanced-features.md) for AI-powered scraping techniques