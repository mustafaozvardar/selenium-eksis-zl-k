# 🕵️‍♂️ EksiSozluk Scraper

This project is a simple web scraper built with Python using Selenium. It extracts and prints the content of popular entries from a specific EksiSozluk page.

## Features ✨

- 🌐 Scrapes the content of entries from EksiSozluk.
- 🕒 Waits for the page to fully load before scraping.
- 📄 Prints the content of each entry to the console.

## Requirements 📦

- Python 3.x
- `selenium` library
- Google Chrome browser
- Chrome WebDriver compatible with your Chrome version

## Installation 🚀

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/eksisozluk-scraper.git
    cd eksisozluk-scraper
    ```

2. Install the required libraries:

    ```bash
    pip install selenium
    ```

3. Download and install [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads):

    - Ensure that the WebDriver version matches your installed Chrome browser version.
    - Add the WebDriver to your system PATH or place it in the same directory as your script.

## Usage 🎤

1. Update the `url` variable in the script to the desired EksiSozluk page:

    ```python
    url="https://eksisozluk1999.com/mert-hakan-yandas--4637778?a=popular"
    ```

2. Run the script:

    ```bash
    python eksi.py
    ```

3. The script will open the specified EksiSozluk page, wait for it to load, and then print the content of each popular entry.

## License 📜

This project is licensed under the MIT License - see the LICENSE file for details.
