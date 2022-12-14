import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint

cid='2c940b44d9004173be0e232225a8f5ba'
clientsec='62ea8892cec54c9ea715df33670a6bba'
creds=SpotifyClientCredentials(client_id=cid,client_secret=clientsec)
sp=spotipy.Spotify(client_credentials_manager=creds)

search_str = input("Enter an artist: ")

result = sp.search(q = 'artist:' + search_str, type = 'artist')
uri=result['artists']['items'][0]['uri']
items=result['artists']['items']
name=result['artists']['items'][0]['name']
response=sp.artist_top_tracks(uri)

for tracks in response['tracks'][:10]:
    print(tracks['name'])
if len (items)>0:
    artists =items[0]
    print(artists['images'][0]['url'])

try:
    related = sp.artist_related_artists(uri)
    print('Related artists for', name)
    for artist in related['artists']:
        print('  ', artist['name'])
except BaseException:
    print("usage show_related.py [artist-name]")

