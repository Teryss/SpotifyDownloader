# SpotifyDownloader
A simple python script to download songs from spotify playlist

# How it works
Using spotipy the script retrieves playlists of a user and fetches songs. <br>
Then using pytube it searches for every song on youtube and downloads highest bitrate audio files with use of threading. <br>
Pytube module sometimes gives an error, but tracks are still downloaded.

# Notes
You need your own <b>client id and client secret</b>. <br> They can be obtained through <a href="https://developer.spotify.com/">this link</a>.
Also, it's a good practice to hide those credentials in environmental variables, but to make usage of this script easier - you can paste it in the right variables instead of None<br>
