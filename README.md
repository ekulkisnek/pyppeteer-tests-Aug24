
# Web Scraping with Pyppeteer

This project demonstrates a simple web scraping application using Pyppeteer, a Python port of Puppeteer. The script navigates to a website and extracts its title using a headless browser.

## Features

- Uses Pyppeteer for browser automation
- Demonstrates basic web scraping capabilities
- Runs Chrome in headless mode

## How It Works

The main script (`main.py`) performs these steps:
1. Launches a Chrome browser instance
2. Opens a new page
3. Navigates to example.com
4. Extracts and prints the page title
5. Closes the browser

## Dependencies

- Python 3.10+
- Pyppeteer 2.0.0+

## Running the Project

Click the "Run" button in Replit to start the application. The script will:
1. Launch a Chrome instance
2. Visit example.com
3. Print the page title
4. Close automatically

## Configuration

The project uses Poetry for dependency management, with configuration in `pyproject.toml`. Chrome is launched with sandbox disabled to work properly in Replit's environment.
