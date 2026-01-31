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
        raise e

def get_video_ids(playlistId):
    maxResults = 50
    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlistId}&maxResults={maxResults}&key={API_KEY}"
    try:
        pageToken = None
        video_ids = []

        while True:
            url = base_url
            if pageToken:
                url += f"&pageToken={pageToken}"
            response = requests.get(url=url)
            response.raise_for_status()
            data = response.json() 

            for item in data.get("items", []):
                video_ids.append(item["contentDetails"]["videoId"])

            pageToken = data.get("nextPageToken")

            if not pageToken:
                break
        return video_ids    
    
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    playlist_id = get_playlist_id()
    #print(get_video_ids(playlist_id))