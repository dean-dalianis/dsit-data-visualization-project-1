import collections
import matplotlib.pyplot as plt
import spotipy

destinations = ['FR', 'ES', 'IT', 'US', 'JP']

# Step 2: Get data on most listened-to music genres in those destinations
spotify = spotipy.Spotify(
    auth='BQDAMSKzxzmUL6FK3sxkpkOzl4UmYPyotuJbXbEyHJwDvT4mJAl94QE1-kmbbaB91iRDnH6Mst47extunCOxB2VFyz_W7rAqhAcAkE8JMKLJtXfQ9zf3t1829Kol2jvqUZnSdaKuciXY0LDM2sLDK41v7ktLgkUsmU5IDs-Kk0TsGQxgNgnMB6fQMqow-1c')
genres_data = []
for destination in destinations:
    genres = []
    for playlist in spotify.category_playlists("toplists", country=destination)['playlists']['items']:
        tracks = spotify.playlist_items(playlist['id'], fields='items(track(name,artists))')
        for track in tracks['items']:
            if track.get('track') and track['track'].get('artists'):
                for artist in track['track']['artists']:
                    genres += spotify.artist(artist['id'])['genres']
    # Count the frequency of each genre
    genre_count = collections.Counter(genres)
    # Get the top 5 most common genres
    top_genres = genre_count.most_common(5)
    genres_data.append({'country': destination, 'top_genres': top_genres})
    print(top_genres)
    print(genres_data)

# Step 3: Create a pie chart for each country
for data in genres_data:
    country_name = data['country']
    top_genres = data['top_genres']
    if not top_genres:
        continue
    labels, sizes = zip(*top_genres)
    fig, ax = plt.subplots()
    ax.set_title(country_name)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    # Save the pie chart as an SVG file
    fig.savefig(f'{country_name}_pie_chart.svg', format='svg')
    plt.close(fig)
