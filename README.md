# Telegram API Scraper

This project is designed to scrape messages from the Mulesoft Telegram group using a Flask backend. It uses the Telegram API for communication and provides a streamlined way to manage Telegram sessions without repeatedly entering OTPs.

## Project Structure

- **`app.py`**  
  This is the main backend file for the project, built using Flask. It handles the server-side functionality and provides endpoints for interacting with the Telegram scraper and other components.

- **`telegram_scraper.py`**  
  This script is responsible for scraping messages from the Mulesoft Telegram group. It interacts with the Telegram API to fetch the desired data.

- **`sessionmaker.py`**  
  This script simplifies Telegram session management. By generating a string session, it ensures that you don't need to re-enter OTPs every time the script is run.

- **`config.py`**  
  This file contains configuration details for the Telegram API, such as API keys, secrets, and other related settings.

## Prerequisites

- Python 3.8+
- Flask
- Telethon (Telegram API Python wrapper)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/rahulkaushik71144/telegramapi.git
   cd telegramapi
