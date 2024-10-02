from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy import create_engine, Column, BigInteger, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from modelPost import TrackCreate

DATABASE_URL = 'postgresql+psycopg2://user:password@localhost:5433/spotify_data'  

# Configuración de SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Track(Base):
    __tablename__ = 'spotify_songs'  
    track_name = Column(Text, primary_key=True)
    artist_name = Column(Text, primary_key=True)
    artist_count = Column(BigInteger)
    released_year = Column(BigInteger)
    released_month = Column(BigInteger)
    released_day = Column(BigInteger)
    in_spotify_playlists = Column(BigInteger)
    in_spotify_charts = Column(BigInteger)
    streams = Column(Text)
    in_apple_playlists = Column(BigInteger)
    in_apple_charts = Column(BigInteger)
    in_deezer_playlists = Column(Text)
    in_deezer_charts = Column(BigInteger)
    in_shazam_charts = Column(Text)
    bpm = Column(BigInteger)
    key = Column(Text)
    mode = Column(Text)
    danceability_percent = Column(BigInteger)
    valence_percent = Column(BigInteger)
    energy_percent = Column(BigInteger)
    acousticness_percent = Column(BigInteger)
    instrumentalness_percent = Column(BigInteger)
    liveness_percent = Column(BigInteger)
    speechiness_percent = Column(BigInteger)

app = FastAPI()

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para consultar los datos
@app.get("/tracks")
def get_tracks(
    db: SessionLocal = Depends(get_db),
    track_name: str = Query(None, description="Filtrar por nombre de canción"),
    artist_name: str = Query(None, description="Filtrar por nombre de artista"),
    released_year: int = Query(None, description="Filtrar por año de lanzamiento"),
    limit: int = Query(default=100, le=100, description="Número máximo de registros por respuesta"),
    offset: int = Query(default=0, ge=0, description="Número de registros para saltar")
):
    
    query = db.query(
        Track.track_name,
        Track.artist_name,
        Track.released_year,
        Track.bpm
    )
        
    if track_name:
        query = query.filter(Track.track_name.ilike(f"%{track_name}%")) 
    if artist_name:
        query = query.filter(Track.artist_name.ilike(f"%{artist_name}%"))
    if released_year:
        query = query.filter(Track.released_year == released_year)

    results = query.offset(offset).limit(limit).all()
        
    tracks = [
        {
            "track_name": track_name,
            "artist_name": artist_name,
            "released_year": released_year,
            "bpm": bpm
        }
        for track_name, artist_name, released_year, bpm in results
    ]

    next_offset = offset + limit if len(tracks) == limit else None
        
    if not tracks:
        raise HTTPException(status_code=404, detail="No tracks found")

    return {
        "data": tracks,
        "limit": limit,
        "offset": offset,
        "next_offset": next_offset
    }
    

