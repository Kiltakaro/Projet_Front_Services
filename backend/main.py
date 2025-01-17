from fastapi import FastAPI
import requests

### Token ###
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMDE3YTQ5ZDJmNmJkMzVmNGUzNGZiMWU0OTM0ZTA5YiIsIm5iZiI6MTczNzEwNTE4My4zODQsInN1YiI6IjY3OGExZjFmYTY0ZmViMTZjOTFkN2M0MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.yETupyK0LYVCDm4-n2UESuzjAORbGIlFffqXaoxN24U"
}
#############

app = FastAPI()


# url = "https://api.themoviedb.org/3/authentication"
# url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&with_genres=16"
url_genres = "https://api.themoviedb.org/3/genre/movie/list?language=en"

response_genres = requests.get(url_genres, headers=headers)
genres = response_genres.json().get("genres", [])


def get_genre_id(genre_name):
    """
    Transforme le nom d'un genre en son Id
    genre_name : String du nom du genre
    """
    for genre in genres:
        if genre["name"].lower() == genre_name.lower():
            return genre["id"]
    return None


# Est ce qu'on considere le cas ou les 3 ont des gouts différents ? 
# Ma vision c'est on regarde les genres et en fonction de si au moins 50% aiment ce genre, on va pouvoir proposer des films avec ce genre.
@app.get("/")
def read_root():
    genre_id = get_genre_id("History")
    url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&with_genres={genre_id}"
    response = requests.get(url, headers=headers)
    return {"message": "Hello, World!", "request_genre": response.json()}

# a refaire
# On va recup les utilisateurs
# on va faire la somme des preferences 
# trouver les ids avec + de 50% 
# avec la string totale 
# faire la requete 
@app.get("/find/movies")
def find_movie_with_genres():
    genre_id = get_genre_id("History")
    url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&with_genres={genre_id}"
    response = requests.get(url, headers=headers)
    return {"message": "Hello, World!", "request_genre": response.json()}



#@app.get("/signup"):