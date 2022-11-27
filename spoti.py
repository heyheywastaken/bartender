import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid='2c940b44d9004173be0e232225a8f5ba'
clientsec='62ea8892cec54c9ea715df33670a6bba'
creds=SpotifyClientCredentials(client_id=cid,client_secret=clientsec)
sp=spotipy.Spotify(client_credentials_manager=creds)

