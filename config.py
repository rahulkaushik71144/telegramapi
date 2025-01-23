
# config.py
import os

class Config:
    # Telegram API Credentials (consider using environment variables)
    API_ID = os.environ.get('TELEGRAM_API_ID', '22939302')
    API_HASH = os.environ.get('TELEGRAM_API_HASH', 'a8fac63e89cb8c003cbcfef3a21e550f')
    PHONE_NUMBER = os.environ.get('TELEGRAM_PHONE_NUMBER', '+919027401844')
    CHANNEL_USERNAME = os.environ.get('TELEGRAM_CHANNEL', 'https://t.me/muleSoftStation')

    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    OUTPUT_FILE = 'job_postings.json'