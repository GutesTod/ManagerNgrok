import requests
import os

if os.getenv("API_NGROK"):
    headers = {
        'Authorization': f'Bearer {os.getenv("API_NGROK")}',
        'Ngrok-Version': '2',
    }

    response = requests.get('https://api.ngrok.com/tunnels', headers=headers)
    print(response.json())
else:
    print("Need Api Ngrok for job!")