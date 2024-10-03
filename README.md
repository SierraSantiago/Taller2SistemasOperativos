Link de ngrok: https://c75b-181-58-39-199.ngrok-free.app/

# FastAPI Music Tracks API

Este proyecto consiste en el desarrollo de una API para gestionar información sobre canciones musicales. Utiliza FastAPI como framework principal y PostgreSQL como sistema de base de datos.
## Instalación y Configuración

### Requisitos Previos
- Python 3.8+
- PostgreSQL 16 (usando Docker)
- Docker y Docker Compose (para gestión de la base de datos)
- WSL (Windows Subsystem for Linux) con Ubuntu

### Pasos de Instalación

1. **Clonar el repositorio**:

    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2. **Crear un entorno virtual e instalar dependencias**:

    ```sh
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. **Configurar la base de datos**:

    - Levantar el contenedor de PostgreSQL con Docker Compose:

        ```sh
        docker-compose up -d
        ```


5. **Levantar la API**:

    ```sh
    uvicorn main:app --reload
    ```

 

## Estructura del Proyecto

- `/model/`: Contiene la definición del modelo Pydantic `TrackCreate` y el modelo SQLAlchemy `Track`.
- `main.py`: Archivo principal que contiene los endpoints de la API.
- `prueba.py`: Script de pruebas para validar el correcto funcionamiento de la API.
- `spotify_api.service`: Archivo `.service` para el autostart del servicio en WSL.

## Uso de la API

### Endpoints Disponibles

1. **Obtener Información de Canciones**  
   **GET /tracks**  
   Devuelve una lista de canciones. Se puede filtrar por parámetros como nombre de canción, nombre del artista y año de lanzamiento.

   **Parámetros**:
   - `track_name` (opcional): Filtrar por nombre de canción.
   - `artist_name` (opcional): Filtrar por nombre de artista.
   - `released_year` (opcional): Filtrar por año de lanzamiento.
   - `limit` (opcional, default=100): Número máximo de registros por respuesta.
   - `offset` (opcional, default=0): Número de registros a omitir.

2. **Mandar informacion de cancion**  
   **POST /tracks**  
   Se envia cancion a la base de datos con este formato:
   ```sh
   [
    {
    "track_name": "Shape of You",
    "artist_name": "Ed Sheeran",
    "artist_count": 1,
    "released_year": 2017,
    "released_month": 1,
    "released_day": 6,
    "in_spotify_playlists": 1,
    "in_spotify_charts": 1,
    "streams": "5000000000",
    "in_apple_playlists": 1,
    "in_apple_charts": 1,
    "in_deezer_playlists": "yes",
    "in_deezer_charts": 1,
    "in_shazam_charts": "yes",
    "bpm": 96,
    "key": "C#",
    "mode": "Major",
    "danceability_percent": 76,
    "valence_percent": 60,
    "energy_percent": 85,
    "acousticness_percent": 5,
    "instrumentalness_percent": 0,
    "liveness_percent": 10,
    "speechiness_percent": 3
      }
    ]

