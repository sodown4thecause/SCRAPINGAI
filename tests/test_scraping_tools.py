"""
Tests for the ScrapingAI library.
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the parent directory to the path so we can import the ScrapingAI module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraping_tools import ScrapingAI

class TestScrapingAI(unittest.TestCase):
    """Test cases for the ScrapingAI class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.scraper = ScrapingAI(user_agent="TestAgent/1.0")
    
    def test_init(self):
        """Test initialization of ScrapingAI."""
        self.assertEqual(self.scraper.user_agent, "TestAgent/1.0")
        self.assertIn("User-Agent", self.scraper.session.headers)
        self.assertEqual(self.scraper.session.headers["User-Agent"], "TestAgent/1.0")
    
    @patch("requests.Session.get")
    def test_fetch_page(self, mock_get):
        """Test fetching a page."""
        # Setup mock
        mock_response = MagicMock()
        mock_response.text = "<html><body>Test Page</body></html>"
        mock_get.return_value = mock_response
        
        # Call the method
        result = self.scraper.fetch_page("https://example.com")
        
        # Assertions
        mock_get.assert_called_once_with("https://example.com")
        self.assertEqual(result, "<html><body>Test Page</body></html>")
    
    def test_parse_html(self):
        """Test parsing HTML."""
        html = "<html><body><h1>Test Heading</h1><p>Test Paragraph</p></body></html>"
        soup = self.scraper.parse_html(html)
        
        self.assertEqual(soup.h1.text, "Test Heading")
        self.assertEqual(soup.p.text, "Test Paragraph")
    
    def test_extract_text(self):
        """Test extracting text using CSS selectors."""
        html = """
        <html>
            <body>
                <h1>Heading 1</h1>
                <h2>Heading 2</h2>
                <p>Paragraph 1</p>
                <p>Paragraph 2</p>
            </body>
        </html>
        """
        soup = self.scraper.parse_html(html)
        
        # Test extracting headings
        headings = self.scraper.extract_text(soup, "h1, h2")
        self.assertEqual(headings, ["Heading 1", "Heading 2"])
        
        # Test extracting paragraphs
        paragraphs = self.scraper.extract_text(soup, "p")
        self.assertEqual(paragraphs, ["Paragraph 1", "Paragraph 2"])
    
    def test_extract_links(self):
        """Test extracting links."""
        html = """
        <html>
            <body>
                <a href="https://example.com">Example</a>
                <a href="/relative">Relative</a>
                <a href="another-relative">Another Relative</a>
                <div>Not a link</div>
            </body>
        </html>
        """
        soup = self.scraper.parse_html(html)
        
        # Test without base URL
        links = self.scraper.extract_links(soup)
        self.assertEqual(links, ["https://example.com"])
        
        # Test with base URL
        links = self.scraper.extract_links(soup, base_url="https://test.com")
        self.assertEqual(links, [
            "https://example.com",
            "https://test.com/relative",
            "https://test.com/another-relative"
        ])

if __name__ == "__main__":
    unittest.main()