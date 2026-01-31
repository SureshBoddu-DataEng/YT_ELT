import requests
import json
import os

from dotenv import load_dotenv

load_dotenv("./.env")
API_KEY = os.getenv("API_KEY")

CHANNEL_HANDLE = "MrBeast"

def get_playlist_id():
    try:
        URL = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url=URL)
        response.raise_for_status()
        data = response.json() 
        # print(json.dumps(data, indent=4))

        channel_items = data["items"]
        channel_playlist_id = channel_items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
        return channel_playlist_id
    
    except requests.exceptions.RequestException as e:
        print(e)

if __name__ == "__main__":
    print(get_playlist_id())