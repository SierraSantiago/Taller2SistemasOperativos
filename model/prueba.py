import requests

BASE_URL = "http://127.0.0.1:8000"

def test_get_tracks():
    print("Testing GET /tracks")
    
    # Caso 1: Sin parámetros, se espera que retorne todos los datos disponibles
    response = requests.get(f"{BASE_URL}/tracks")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "data" in data, "Response JSON does not contain 'data' field"
    assert isinstance(data["data"], list), f"Expected 'data' to be a list, got {type(data['data'])}"
    print("Passed: GET /tracks without parameters")
    
    # Caso 2: Con parámetros que no existen
    response = requests.get(f"{BASE_URL}/tracks?track_name=NonExistentTrack")
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
    print("Passed: GET /tracks with non-existent track_name")
    
    # Caso 3: Con un track_name válido, se espera al menos un resultado
    response = requests.get(f"{BASE_URL}/tracks?track_name=Shape of You")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "data" in data, "Response JSON does not contain 'data' field"
    assert len(data["data"]) > 0, "Expected at least one track in response, but got none"
    print("Passed: GET /tracks with existing track_name")


def test_create_tracks():
    print("Testing POST /tracks")
    
    # Caso 3: Datos correctos
    valid_data = [
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

    response = requests.post(f"{BASE_URL}/tracks", json=valid_data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Passed: POST /tracks with valid data")

    # Caso 4: Datos incorrectos 
    invalid_data = [
        {
            "track_name": "Shape of You",
            "artist_name": "Ed Sheeran",
            "artist_count": "NotANumber",  # Esto debería ser un número
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

    response = requests.post(f"{BASE_URL}/tracks", json=invalid_data)
    assert response.status_code == 422, f"Expected 422, got {response.status_code}"
    print("Passed: POST /tracks with invalid data")

if __name__ == "__main__":
    test_get_tracks()
    test_create_tracks()
    print("All tests passed!")
