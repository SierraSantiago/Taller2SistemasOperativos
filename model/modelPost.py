from pydantic import BaseModel
class TrackCreate(BaseModel):
    track_name: str
    artist_name: str
    artist_count: int
    released_year: int
    released_month: int
    released_day: int
    in_spotify_playlists: int  
    in_spotify_charts: int      
    streams: str                
    in_apple_playlists: int     
    in_apple_charts: int        
    in_deezer_playlists: str    
    in_deezer_charts: int       
    in_shazam_charts: str       
    bpm: int                    
    key: str                    
    mode: str                   
    danceability_percent: int    
    valence_percent: int         
    energy_percent: int          
    acousticness_percent: int    
    instrumentalness_percent: int 
    liveness_percent: int         
    speechiness_percent: int      
