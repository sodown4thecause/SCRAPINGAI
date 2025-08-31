# API Reference

This page provides detailed documentation for the SCRAPINGAI API.

## ScrapingAI Class

The main class for AI-powered web scraping operations.

### Constructor

```python
ScrapingAI(user_agent=None)
```

**Parameters:**
- `user_agent` (str, optional): Custom user agent string. If None, a default one will be used.

### Methods

#### fetch_page

```python
fetch_page(url)
```

Fetch a web page and return its HTML content.

**Parameters:**
- `url` (str): The URL to fetch.

**Returns:**
- str: The HTML content of the page.

**Raises:**
- `requests.exceptions.RequestException`: If the request fails.

#### parse_html

```python
parse_html(html)
```

Parse HTML content using BeautifulSoup.

**Parameters:**
- `html` (str): HTML content to parse.

**Returns:**
- `BeautifulSoup`: BeautifulSoup object.

#### extract_text

```python
extract_text(soup, selector)
```

Extract text from elements matching a CSS selector.

**Parameters:**
- `soup` (BeautifulSoup): BeautifulSoup object.
- `selector` (str): CSS selector.

**Returns:**
- List[str]: List of extracted text strings.

#### extract_links

```python
extract_links(soup, base_url="")
```

Extract all links from a page.

**Parameters:**
- `soup` (BeautifulSoup): BeautifulSoup object.
- `base_url` (str, optional): Base URL to prepend to relative links.

**Returns:**
- List[str]: List of links.

#### scrape_with_delay

```python
scrape_with_delay(urls, selector, delay_range=(1, 3))
```

Scrape multiple URLs with a random delay between requests.

**Parameters:**
- `urls` (List[str]): List of URLs to scrape.
- `selector` (str): CSS selector to extract content.
- `delay_range` (tuple, optional): Tuple of (min_delay, max_delay) in seconds.

**Returns:**
- Dict[str, List[str]]: Dictionary mapping URLs to extracted content.