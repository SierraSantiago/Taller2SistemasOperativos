import pandas as pd
import chardet
from sqlalchemy import create_engine

with open('Data/spotify-2023.csv', 'rb') as f:
    result = chardet.detect(f.read())
encoding = result['encoding']

df = pd.read_csv('Data/spotify-2023.csv', encoding=encoding)

df.columns = ['track_name', 'artist_name', 'artist_count', 'released_year', 'released_month', 'released_day',
              'in_spotify_playlists', 'in_spotify_charts', 'streams', 'in_apple_playlists', 'in_apple_charts',
              'in_deezer_playlists', 'in_deezer_charts', 'in_shazam_charts', 'bpm', 'key', 'mode', 
              'danceability_percent', 'valence_percent', 'energy_percent', 'acousticness_percent',
              'instrumentalness_percent', 'liveness_percent', 'speechiness_percent']


engine = create_engine('postgresql+psycopg2://user:password@localhost:5433/spotify_data')



df.to_sql('spotify_songs', engine, if_exists='replace', index=False)

print("Datos cargados correctamente en la base de datos.")
