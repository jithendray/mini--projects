# Import libraries to access authorised spotify data
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# specify the spotipy client details
client_id= "<secret>"
client_secret= "<secret>"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# spotify object to access API
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# choose artist
name = 'Black Sabbath'
result = sp.search(name) #search query
# print(result['tracks']['items'][0]['artists'])

#Extracting Artist's uri
artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
#print(artist_uri)

#Pulling all of the artist's albums
sp_albums = sp.artist_albums(artist_uri, album_type='album')
#Storing artist's albums' names' and uris in separate lists
album_names = []
album_uris = []
for i in range(len(sp_albums['items'])):
    album_names.append(sp_albums['items'][i]['name'])
    album_uris.append(sp_albums['items'][i]['uri'])    
# print(album_names)
#Keeping names and uris in same order to keep track of duplicate albums
# removing the duplicate ones!

del album_names[3]
del album_names[3]
del album_names[3]
del album_names[3]
del album_names[3]
del album_names[3]
del album_uris[3]
del album_uris[3]
del album_uris[3]
del album_uris[3]
del album_uris[3]
del album_uris[3]
# print(album_names)

# getting song details from the album uris
def albumSongs(uri):
    album = uri 
    spotify_albums[album] = {} 
    #Creating keys-values of empty lists inside nested dictionary for album
    spotify_albums[album]['album'] = [] 
    spotify_albums[album]['track_number'] = []
    spotify_albums[album]['id'] = []
    spotify_albums[album]['name'] = []
    spotify_albums[album]['uri'] = []
    tracks = sp.album_tracks(album) #pull data on album tracks
    for n in range(len(tracks['items'])): 
            spotify_albums[album]['album'].append(album_names[album_count])
            spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
            spotify_albums[album]['id'].append(tracks['items'][n]['id'])
            spotify_albums[album]['name'].append(tracks['items'][n]['name'])
            spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])

spotify_albums = {}
album_count = 0
for i in album_uris:
    albumSongs(i)
    print("Album " + str(album_names[album_count]) + " songs has been added to the dictionary")
    album_count+=1

# defining the audio features
def audio_features(album):
    #Adding new key-values to store audio features
    spotify_albums[album]['acousticness'] = []
    spotify_albums[album]['danceability'] = []
    spotify_albums[album]['energy'] = []
    spotify_albums[album]['instrumentalness'] = []
    spotify_albums[album]['liveness'] = []
    spotify_albums[album]['loudness'] = []
    spotify_albums[album]['speechiness'] = []
    spotify_albums[album]['tempo'] = []
    spotify_albums[album]['valence'] = []
    spotify_albums[album]['popularity'] = []
    #creating a track counter
    track_count = 0
    for track in spotify_albums[album]['uri']:
        #pulling audio features per track
        features = sp.audio_features(track)
        spotify_albums[album]['acousticness'].append(features[0]['acousticness'])
        spotify_albums[album]['danceability'].append(features[0]['danceability'])
        spotify_albums[album]['energy'].append(features[0]['energy'])
        spotify_albums[album]['instrumentalness'].append(features[0]['instrumentalness'])
        spotify_albums[album]['liveness'].append(features[0]['liveness'])
        spotify_albums[album]['loudness'].append(features[0]['loudness'])
        spotify_albums[album]['speechiness'].append(features[0]['speechiness'])
        spotify_albums[album]['tempo'].append(features[0]['tempo'])
        spotify_albums[album]['valence'].append(features[0]['valence'])
        pop = sp.track(track)
        spotify_albums[album]['popularity'].append(pop['popularity'])
        track_count+=1

import time
import numpy as np
sleep_min = 2
sleep_max = 5
start_time = time.time()
request_count = 0
for i in spotify_albums:
    audio_features(i)
    request_count+=1
    if request_count % 5 == 0:
        print(str(request_count) + " playlists completed")
        time.sleep(np.random.uniform(sleep_min, sleep_max))
        print('Loop #: {}'.format(request_count))
        print('Elapsed Time: {} seconds'.format(time.time() - start_time))


dic_df = {}
dic_df['album'] = []
dic_df['track_number'] = []
dic_df['id'] = []
dic_df['name'] = []
dic_df['uri'] = []
dic_df['acousticness'] = []
dic_df['danceability'] = []
dic_df['energy'] = []
dic_df['instrumentalness'] = []
dic_df['liveness'] = []
dic_df['loudness'] = []
dic_df['speechiness'] = []
dic_df['tempo'] = []
dic_df['valence'] = []
dic_df['popularity'] = []
for album in spotify_albums: 
    for feature in spotify_albums[album]:
        dic_df[feature].extend(spotify_albums[album][feature])

#####################################################################
        
import pandas as pd
df = pd.DataFrame.from_dict(dic_df)
df['artist'] = name
# data-cleaning
df1 = df[df['album']=='Black Sabbath']
df2 = df[df['album']=='Paranoid']
df3 = df[df['album']=='Master of Reality']
df4 = df[df['album']=='Vol. 4']
df5 = df[df['album']=='Sabbath Bloody Sabbath']
df6 = df[df['album']=='Technical Ecstasy']
df7 = df[df['album']=='Never Say Die!']
df8 = df[df['album']=='Live At Last']
df9 = df[df['album']=='Born Again (Deluxe Edition)']
df10 = df[df['album']=='Seventh Star']
df11 = df[df['album']=='The Eternal Idol']
df12 = df[df['album']=='Past Lives (Deluxe Edition)']
df13 = df[df['album']=='13']
df14 = df[df['album']=='The End (Live)']
df1 = df1.reset_index()
df1 = df1.drop('index', axis=1)
df2 = df2.reset_index()
df2 = df2.drop('index', axis=1)
df3 = df3.reset_index()
df3 = df3.drop('index', axis=1)
df4 = df4.reset_index()
df4 = df4.drop('index', axis=1)
df5 = df5.reset_index()
df5 = df5.drop('index', axis=1)
df6 = df6.reset_index()
df6 = df6.drop('index', axis=1)
df7 = df7.reset_index()
df7 = df7.drop('index', axis=1)
df8 = df8.reset_index()
df8 = df8.drop('index', axis=1)
df9 = df9.reset_index()
df9 = df9.drop('index', axis=1)
df10 = df10.reset_index()
df10 = df10.drop('index', axis=1)
df11 = df11.reset_index()
df11 = df11.drop('index', axis=1)
df12 = df12.reset_index()
df12 = df12.drop('index', axis=1)
df13 = df13.reset_index()
df13 = df13.drop('index', axis=1)
df14 = df14.reset_index()
df14 = df14.drop('index', axis=1)

frames = [df1, df2, df3,df4,df5,df6,df7,df8,df9,df10,df11,df13]
f_df = pd.concat(frames)
f_df = f_df.reset_index()
f_df = f_df.drop('index',axis=1)
final_df = f_df.drop_duplicates('name').sort_index()

#####################################################################

# saving into a dataframe
final_df.to_csv('black-sabbath.csv', index=False)




