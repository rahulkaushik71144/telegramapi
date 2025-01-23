from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import asyncio
import os
from telegram_scraper import TelegramJobScraper
from config import Config
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

scraper = TelegramJobScraper()

@app.route('/api/job-postings', methods=['GET'])
def get_job_postings():
    """
    Fetch and return job postings
    Query Parameters:
    - refresh (optional): If 'true', forces a new scrape
    """
    refresh = request.args.get('refresh', 'false').lower() == 'true'
    
    try:
        if refresh or not os.path.exists(Config.OUTPUT_FILE):
            # Run async function in event loop
            job_postings = asyncio.run(scraper.get_job_postings())
        else:
            # Read from existing file
            with open(Config.OUTPUT_FILE, 'r') as f:
                job_postings = json.load(f)
        
        return jsonify(job_postings)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/job-postings/download', methods=['GET'])
def download_job_postings():
    """
    Download job postings JSON file
    """
    try:
        return send_file(Config.OUTPUT_FILE, as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "No job postings file found"}), 404

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint
    """
    return jsonify({
        "status": "healthy",
        "service": "Telegram Job Scraper",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
