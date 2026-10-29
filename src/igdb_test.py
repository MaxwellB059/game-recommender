import os
import json
import requests
from dotenv import load_dotenv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")

url = "https://id.twitch.tv/oauth2/token"

params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

response = requests.post(url, data=params, timeout=15)
response.raise_for_status()

access_token = response.json()["access_token"]

print("Successfully obtained access token!")

# Request platform information from IGDB
igdb_url = "https://api.igdb.com/v4/platforms"

headers = {
    "Client-ID": client_id,
    "Authorization": f"Bearer {access_token}"
}

query = "fields id,name; where id > 0; sort id asc; limit 500;"

response = requests.post(
    igdb_url,
    headers=headers,
    data=query,
    timeout=15
)

response.raise_for_status()
platforms = response.json()
for platform in platforms:
    print(f"{platform['id']}: {platform['name']}")
print("Total platforms retrieved:", len(platforms))

PLATFORMS_PATH = PROJECT_ROOT / "data" / "processed" / "platforms.json"
PLATFORMS_PATH.parent.mkdir(parents=True, exist_ok=True)
with PLATFORMS_PATH.open("w", encoding="utf-8") as file:
    json.dump(platforms, file, indent=2)


