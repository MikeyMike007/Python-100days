# Program adds the billboard of a date to a spotify playlist

from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
import spotipy

date = input("Date:")

PARSER = "html.parser"
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
PLAYLIST_NAME = f"Billboard Top 100 {date}"
YEAR = date[:4]


response = requests.get(url=URL)
soup = BeautifulSoup(response.text, PARSER)

songs = soup.select("li ul li h3")
song_names = [track.getText().strip() for track in songs]

scope = "playlist-modify-private"

# Authenticate from enviroment variables
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Determine user_id
user_id = spotify.current_user()["id"]

# Store song urls here
song_urls = []

for song in song_names:
    items = spotify.search(q=f"track: {song} year: {YEAR}", type="track")["tracks"][
        "items"
    ]
    if len(items) > 0:
        song_urls.append(items[0]["uri"])

playlist_id = spotify.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False
)["id"]
#
spotify.playlist_add_items(playlist_id=playlist_id, items=song_urls)
