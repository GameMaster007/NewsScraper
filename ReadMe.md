# NewsScraper

## Overview

**NewsScraper** is a Python-based asynchronous application designed to fetch and print news articles from specified RSS feeds. It leverages the power of asynchronous programming to efficiently handle multiple HTTP requests, making it an ideal tool for aggregating news content from various sources.

## Features

- **Asynchronous Fetching**: Utilizes `aiohttp` for non-blocking HTTP requests, significantly improving performance when dealing with multiple feeds.
- **RSS Feed Parsing**: Employs `feedparser` to parse RSS feeds, extracting relevant information such as article titles and links.
- **Keyword Filtering**: Allows users to filter the fetched news articles by a specific keyword, enhancing the relevance of the output.
- **Logging**: Incorporates logging to track the application's progress and report any errors encountered during execution.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `aiohttp` library
- `feedparser` library

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/GameMaster007/NewsScraper.git
   ```
2. Navigate to the project directory:
   ```
   cd NewsScraper
   ```
3. Install the required Python libraries:
   ```
   pip install aiohttp feedparser
   ```

### Usage

To run the NewsScraper, simply execute the `NewsScraper.py` script. You will be prompted to enter a keyword to filter the news articles by. If you wish to see all articles without filtering, simply press Enter when prompted for a keyword.

```
python NewsScraper.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
