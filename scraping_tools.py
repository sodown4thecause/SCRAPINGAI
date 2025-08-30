"""
SCRAPINGAI - Web Scraping Tools

This module provides various tools and utilities for web scraping using AI techniques.
"""

import requests
from bs4 import BeautifulSoup
import re
import json
import time
import random
from typing import List, Dict, Any, Optional

class ScrapingAI:
    """Main class for AI-powered web scraping operations."""
    
    def __init__(self, user_agent: Optional[str] = None):
        """
        Initialize the ScrapingAI instance.
        
        Args:
            user_agent: Custom user agent string. If None, a default one will be used.
        """
        self.session = requests.Session()
        self.user_agent = user_agent or "ScrapingAI/1.0 (https://github.com/sodown4thecause/SCRAPINGAI)"
        self.session.headers.update({"User-Agent": self.user_agent})
        
    def fetch_page(self, url: str) -> str:
        """
        Fetch a web page and return its HTML content.
        
        Args:
            url: The URL to fetch.
            
        Returns:
            The HTML content of the page.
        """
        response = self.session.get(url)
        response.raise_for_status()
        return response.text
    
    def parse_html(self, html: str) -> BeautifulSoup:
        """
        Parse HTML content using BeautifulSoup.
        
        Args:
            html: HTML content to parse.
            
        Returns:
            BeautifulSoup object.
        """
        return BeautifulSoup(html, "html.parser")
    
    def extract_text(self, soup: BeautifulSoup, selector: str) -> List[str]:
        """
        Extract text from elements matching a CSS selector.
        
        Args:
            soup: BeautifulSoup object.
            selector: CSS selector.
            
        Returns:
            List of extracted text strings.
        """
        elements = soup.select(selector)
        return [element.get_text(strip=True) for element in elements]
    
    def extract_links(self, soup: BeautifulSoup, base_url: str = "") -> List[str]:
        """
        Extract all links from a page.
        
        Args:
            soup: BeautifulSoup object.
            base_url: Base URL to prepend to relative links.
            
        Returns:
            List of links.
        """
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("http"):
                links.append(href)
            elif base_url:
                links.append(f"{base_url.rstrip('/')}/{href.lstrip('/')}")
        return links
    
    def scrape_with_delay(self, urls: List[str], selector: str, delay_range: tuple = (1, 3)) -> Dict[str, List[str]]:
        """
        Scrape multiple URLs with a random delay between requests.
        
        Args:
            urls: List of URLs to scrape.
            selector: CSS selector to extract content.
            delay_range: Tuple of (min_delay, max_delay) in seconds.
            
        Returns:
            Dictionary mapping URLs to extracted content.
        """
        results = {}
        for url in urls:
            try:
                html = self.fetch_page(url)
                soup = self.parse_html(html)
                results[url] = self.extract_text(soup, selector)
                
                # Random delay to be respectful
                if url != urls[-1]:  # No need to delay after the last request
                    time.sleep(random.uniform(*delay_range))
            except Exception as e:
                results[url] = [f"Error: {str(e)}"]
        return results

# Example usage
if __name__ == "__main__":
    scraper = ScrapingAI()
    html = scraper.fetch_page("https://example.com")
    soup = scraper.parse_html(html)
    headings = scraper.extract_text(soup, "h1, h2, h3")
    print(f"Found {len(headings)} headings on the page:")
    for heading in headings:
        print(f"- {heading}")