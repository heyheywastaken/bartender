import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint

cid='2c940b44d9004173be0e232225a8f5ba'
clientsec='62ea8892cec54c9ea715df33670a6bba'
creds=SpotifyClientCredentials(client_id=cid,client_secret=clientsec)
sp=spotipy.Spotify(client_credentials_manager=creds)

search_str = input("")

result = sp.search(q = 'artist:' + search_str, type = 'artist')
url=print(result['artists']['items'][0]['external_urls']['spotify'])
print(type(url))
pprint.pprint(result)


# uri=url.split('/')
# print(uri)
# response=sp.artist_top_tracks(url)
# print(response)