from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"

date = input("What date do u want to travel to?(YYYY-MM-DD)")

response = requests.get(url="{}/".format(URL + date))
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_titles = [song.getText().strip() for song in titles]

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_secret=CLIENT_SECRET,
                                               client_id=CLIENT_ID,
                                               scope="user-library-read playlist-modify-private",
                                               show_dialog=True,
                                               redirect_uri=REDIRECT_URI,
                                               cache_path="token.txt")
                     )
user = sp.current_user()
user_id = user["id"]

song_uris = []
year = date.split("-")[0]
count = 0
for song in song_titles:
    result = sp.search(q="track: {} year: {}".format(song, year), type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        count += 1
    except IndexError:
        print("Sorry, {} doesn't exist on Spotify. Skip".format(song))

print(count)
playlist = sp.user_playlist_create(user=user_id, name="{} Billboard 100".format(date), public=False)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)
