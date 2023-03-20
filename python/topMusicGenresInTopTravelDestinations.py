import collections

import matplotlib.pyplot as plt
import spotipy
from wordcloud import WordCloud

destinations = ['FR', 'ES', 'IT', 'US', 'JP']
countries = {'FR': 'France', 'ES': 'Spain', 'IT': 'Italy', 'US': 'United States', 'JP': 'Japan'}

AUTH_TOKEN = 'BQAeDYWiKwHJMpOBXFPZtzVBMNoWfTmgh04RK3W-BzApcYP1-fdOhwP8Lv--N9e7g3uTi_qN0AH5mo-1iiifoBfvBQ-8EDl2Ug_EBm4KuTnwyOOGhPAnQiKhD2AOX5drzL_7oezZLwdLyNE3VhnRi5VE_VrICjOPJfF8rQfoYGIjyjWwC3VrS2N164p5B7s'

spotify = spotipy.Spotify(auth=AUTH_TOKEN, requests_timeout=10, retries=3)


def generate_charts(destination):
    genres = []
    for playlist in spotify.category_playlists("toplists", country=destination)['playlists']['items']:
        tracks = spotify.playlist_items(playlist['id'], fields='items(track(name,artists))')
        for track in tracks['items']:
            if track.get('track') and track['track'].get('artists'):
                for artist in track['track']['artists']:
                    genres += spotify.artist(artist['id'])['genres']
    genre_count = collections.Counter(genres)
    top_genres = genre_count.most_common(10)

    if top_genres:
        labels, sizes = zip(*top_genres)
        fig, ax = plt.subplots()
        ax.set_title(countries[destination])
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        fig.savefig(f'{destination}_pie_chart.svg', format='svg')
        plt.close(fig)

        wordcloud = WordCloud(background_color='white', width=800, height=800).generate_from_frequencies(genre_count)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title(countries[destination])
        fig.savefig(f'{destination}_wordcloud.svg', format='svg')
        plt.close(fig)


for dest in destinations:
    generate_charts(dest)
