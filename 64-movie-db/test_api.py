import requests
import os

API_KEY = os.environ.get("MOVIEDB_API_KEY")
MOVIE_API_URL = "https://api.themoviedb.org/3/search/movie"

params = {"api_key": API_KEY, "query": "batman"}
response = requests.get(url=MOVIE_API_URL, params=params).json()

for movie in response["results"]:
    print(f"{movie}\n")
