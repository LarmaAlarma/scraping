# Scraping

This project demonstrates web scraping by extracting data from a quotes website and presenting it through a simple GUI.

## Project Overview

- **Website Scraped**: [Quotes to Scrape](https://quotes.toscrape.com/)
- **Objective**: 
  - Scrape quotes and their authors from the website.
  - Save the scraped data to a CSV file.
  - Create a simple GUI to allow users to select an author and view their quotes.

## Features

- **Web Scraping**: Utilizes BeautifulSoup to fetch and parse HTML content.
- **Data Storage**: Quotes are stored in a CSV file for easy access.
- **Graphical User Interface**: Built with Tkinter for user-friendly interaction.

## Installation Instructions

### Prerequisites

1. **Python 3**: Ensure you have Python 3 installed on your system.
2. **Virtual Environment**: It is recommended to use a virtual environment for managing dependencies.
3. **Python3-tk**: If You are using Linux like i do ensure that u install outside venv Python3-tk
    ```bash
    sudo apt install Python3-tk

### Setting Up the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd scraping
