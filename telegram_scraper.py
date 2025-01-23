import re
import json
import asyncio
from telethon import TelegramClient
from typing import List, Dict, Any
from config import Config
import os
from telethon.sessions import StringSession



class TelegramJobScraper:
    def __init__(self):
        with open('session_string.session', 'r') as f:
            session_string = f.read().strip()


          # Replace with your generated string
        
        # Remove existing session file
        session_file = 'session_name.session'
        if os.path.exists(session_file):
            os.remove(session_file)
        
        # Create client using StringSession
        self.client = TelegramClient(StringSession(session_string), Config.API_ID, Config.API_HASH)
        self.email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        self.job_keywords = ['job', 'hiring', 'recruiting', 'position', 'role', 'vacancy', 'career']

    async def fetch_filtered_messages(self):
        print(f"Connecting with Channel: {Config.CHANNEL_USERNAME}")
        await self.client.start(Config.PHONE_NUMBER)
        
        messages = await self.client.get_messages(Config.CHANNEL_USERNAME, limit=5)
        print(f"Total Messages Found: {len(messages)}")
        
        filtered_messages = []
    
        for message in messages:
            if message.text:
                print("Full Message Text:", message.text)  # Print full message text
                
                # Relaxed filtering criteria
                has_job_keyword = any(keyword in message.text.lower() for keyword in self.job_keywords)
                has_mulesoft = 'mulesoft' in message.text.lower()
            
                if has_job_keyword or has_mulesoft:
                    # print("Message Matched Criteria!")
                    filtered_messages.append({
                        "sender_id": message.sender_id,
                        "text": message.text,
                        "date": str(message.date),
                    })
    
        return filtered_messages

    def extract_info_from_job_posting(self, text: str) -> Dict[str, Any]:
        # More flexible email extraction
        email_match = re.search(r'\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b', text)
        email = email_match.group(1) if email_match else "No email provided"

        # More flexible role and experience extraction
        role_exp_matches = re.findall(r'(Mulesoft\s*[^\d\n]*)\s*(\d+)(?:\s*\+?)?\s*(?:years?|yrs?)', text, re.IGNORECASE)

        roles_experience = []
        for match in role_exp_matches:
            role = ' '.join(match[0].split())
            years = match[1]
            roles_experience.append(f"{role}, experience {years}+ years")
            print("hehehhe uwuuwuuwuw")
            print(email)
            print(roles_experience)

        return {
            'description': text.strip(),
            'emailTo': email,
            'requirements': roles_experience
        }

    async def get_job_postings(self):
        try:
            filtered_messages = await self.fetch_filtered_messages()
            processed_entries = []
            
            for entry in filtered_messages:
                job_info = self.extract_info_from_job_posting(entry['text'])
                processed_entries.append(job_info)
            
            # Save to file
            with open(Config.OUTPUT_FILE, 'w') as output_file:
                json.dump(processed_entries, output_file, indent=2)
            print(processed_entries)
            return processed_entries
        
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

async def main():
    scraper = TelegramJobScraper()
    messages = await scraper.fetch_filtered_messages()
    print("Filtered Messages:", messages)
    extracted_info = scraper.extract_info_from_job_posting(messages[0]['text'])
    print("Extracted Info:", extracted_info)
    get_job_postings = await scraper.get_job_postings()
    print("Job Postings:", get_job_postings)

if __name__ == "__main__":
    asyncio.run(main())

