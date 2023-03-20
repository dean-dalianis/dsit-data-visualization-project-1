import requests
import spotipy
import matplotlib.pyplot as plt
import collections
import folium

destinations = ['FR']#, 'ES', 'IT', 'USA', 'JP']

# Step 2: Get data on most listened-to music genres in those destinations
spotify = spotipy.Spotify(auth='BQDAMSKzxzmUL6FK3sxkpkOzl4UmYPyotuJbXbEyHJwDvT4mJAl94QE1-kmbbaB91iRDnH6Mst47extunCOxB2VFyz_W7rAqhAcAkE8JMKLJtXfQ9zf3t1829Kol2jvqUZnSdaKuciXY0LDM2sLDK41v7ktLgkUsmU5IDs-Kk0TsGQxgNgnMB6fQMqow-1c')
genres_data = []
for destination in destinations:
    genres = []
    for playlist in spotify.category_playlists("toplists", country=destination)['playlists']['items']:
        tracks = spotify.playlist_items(playlist['id'], fields='items(track(name,artists))')
        for track in tracks['items']:
            if track['track']:
                if track['track']['artists']:
                    for artist in track['track']['artists']:
                        genres += spotify.artist(artist['id'])['genres']
    # Count the frequency of each genre
    genre_count = collections.Counter(genres)
    # Get the top 5 most common genres
    top_genres = genre_count.most_common(5)
    genres_data.append({'country': destination, 'top_genres': top_genres})
    print(top_genres)
    print(genres_data)

# Step 3: Create a choropleth map visualization
m = folium.Map(location=[48.864716, 2.349014], zoom_start=2)
for data in genres_data:
    country_name = data['country']
    top_genres = data['top_genres']
    if not top_genres:
        continue
    folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/python-visualization/folium/master/examples/data',
        name=country_name,
        data=top_genres,
        columns=[('genre', 'count')],
        key_on='feature.properties.name',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Top 5 Music Genres'
    ).add_to(m)

# Save the map as an HTML file
m.save('music_genre_map.html')
