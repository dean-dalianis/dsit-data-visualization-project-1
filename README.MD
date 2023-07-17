# DSIT Data Visualization Project 1

This is a basic website built using HTML5, CSS, SVG, Javascript, and jQuery for the *M126 Data Visualization* course
taught by Professor Maria Roussou as part of the *Data Science and Information Technologies* M.Sc. in Department of
Informatics and Telecommunications at University of Athens.

## Top Music Genres in Top Travel Destinations

As part of the project, I wrote a
simple [Python Spotify Analysis Script](python/topMusicGenresInTopTravelDestinations.py) which generates charts and word
clouds based on Spotify playlists for selected destinations. The code utilizes the Spotipy library to retrieve playlists
from the *"toplists"* category for each destination country. It then extracts the genres associated with the tracks in
these playlists and creates visual representations of the most common genres. The resulting charts, including pie charts
and word clouds, are saved as SVG files for each destination.

## Pages

The three pages of the website are:

- **index.html**: Includes 3 paragraphs about me and a picture of myself.
- **music-genres-per-country.html**: Includes a data-driven visualization images generated using *
  *topMusicGenresInTopTravelDestinations.py**.
- **whack-a-shape.html**: Includes a small game built using SVGs and jQuery.
- **superpowers-review.html**: Includes thoughts for the paper Superpowers as Inspiration for Visualization.
- **credits.html**: Includes credit to all the sources used to build the website, including licenses.