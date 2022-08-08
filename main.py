import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube, Search
from threading import Thread
import os
client_id = None
client_secret = None
auth_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

user = input("Enter your username: ")

playlists = sp.user_playlists(user)
items = playlists['items']
choices = []
uris = []
i = 0
print("all available playlists: ")
for playlist in items:
    print(f"{i}: {playlist['name']}")
    uris.append(playlist['uri'])
    i += 1

index = int(input('Which playlist you want to download? (ex. 1): '))

playlist_uid = uris[index]
results = sp.user_playlist_tracks(user,playlist_uid)
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

tracks_fullinfo = []
for track in tracks:
    tracks_fullinfo.append(f"{track['track']['name']} - {track['track']['artists'][0]['name']}")
highest_bitrate_itag = 251 #160kbps opus audio file

download_path = os.path.dirname(os.path.abspath(__file__)) + '\songs' 
download_counter = 0
all_downloads = len(tracks_fullinfo)
def search_and_download(track, all_downloads, path):
    global download_counter
    s = Search(track)
    yt = s.results[0]
    stream = yt.streams.get_by_itag(highest_bitrate_itag)
    stream.download(path)
    download_counter += 1
    print(f"Downloaded {download_counter} out of {all_downloads}")

print("Starting downloading")
threads = []
for track in tracks_fullinfo:
    t = Thread(target=search_and_download, args=[track, all_downloads, download_path])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

print("All done :) Songs should be in the songs folder near the script!")
