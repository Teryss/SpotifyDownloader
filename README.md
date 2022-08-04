# SpotifyDownloader
A simple python script to download songs from spotify playlist

# How it works
Using spotipy the script retrieves playlists of a user and fetches songs. <br>
Then using pytube it searches for every song on youtube and downloads highest bitrate audio files with use of threading. <br>
Pytube module sometimes gives an error, but tracks are still downloaded.

# Notes
Please note that you need a client id and client secret. <br> They can be obtained through <a href="https://developer.spotify.com/">this link</a>.
Also you're adviced to hide those credentials in environmental variables, but if it's not an option - paste correct values instead of None to the correct variable in script. <br>
In this case I would also advice you to create a fresh account with VPN/tor so it doesn't get traced back to you or your data in case of leakage.
