import requests
response = requests.get('http://localhost:5000/api/job-postings')
print(response.json())