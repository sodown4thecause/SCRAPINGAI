# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project structure
- Basic scraping functionality
- Documentation framework
- Testing framework
- CI/CD workflows

## [0.1.0] - 2025-08-30

### Added
- Initial release
- Core `ScrapingAI` class with basic functionality:
  - `fetch_page`: Fetch a web page and return its HTML content
  - `parse_html`: Parse HTML content using BeautifulSoup
  - `extract_text`: Extract text from elements matching a CSS selector
  - `extract_links`: Extract all links from a page
  - `scrape_with_delay`: Scrape multiple URLs with a random delay between requests
- Basic documentation
- Unit tests
- Example scripts

[Unreleased]: https://github.com/sodown4thecause/SCRAPINGAI/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/sodown4thecause/SCRAPINGAI/releases/tag/v0.1.0