from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
year = date[:4]
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
print(URL)
response = requests.get(URL)
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")

song_titles = [song_title.getText().replace("\n", "").replace("\t", "") for song_title in soup.find_all(name="h3", class_="a-no-trucate")]
artists_names = [artist_name.getText().replace("\n", "").replace("\t", "") for artist_name in soup.find_all(name="span", class_="a-no-trucate")]
print(song_titles)
print(artists_names)
c_id = "86a5e0a29ae8424cbfa6903d86433865"
c_secret = "dd0724fbd2fb4af385d5ce9eb8977eed"
redirect_uri = "http://example.com"
scope = "playlist-modify-private"

# sp.get_cached_token()
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=c_id,
        client_secret=c_secret,
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uri = []
for number in range(len(song_titles)):
    try:
        song = sp.search(q=f"track:{song_titles[number]} artist:{artists_names[number]}", offset=0, type="track", limit=1, market=None)
        song_link = song['tracks']['items'][0]['uri']
        song_uri.append(song_link)
    except:
        pass

playlist_billboard = sp.user_playlist_create(
    user=user_id, 
    name=f"{date} Billboard 100",
    public=False, 
    description=f"Billboard Hot 100 on {date}, go back in time"
    )
playlist_id = playlist_billboard["id"]
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_uri, position=None)
# Here, your task is to authenticate your project with the spotify and get access to the user's username.
# Here, you need access to the user account in order to include playlist into that account.
# Therefore, you need to go through authentication process, you need client id and client secret.
# For making things easier, we are using spotipy module.