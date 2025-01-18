from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import requests
import psycopg2
from psycopg2 import sql
from pydantic import BaseModel
from typing import List
from userModel import UserBaseModel

# Configuration PostgreSQL
DB_CONFIG = {
    'dbname': 'database',
    'user': 'user',
    'password': 'password',
    'host': 'localhost',
    'port': 5432
}

### Token ###
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMDE3YTQ5ZDJmNmJkMzVmNGUzNGZiMWU0OTM0ZTA5YiIsIm5iZiI6MTczNzEwNTE4My4zODQsInN1YiI6IjY3OGExZjFmYTY0ZmViMTZjOTFkN2M0MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.yETupyK0LYVCDm4-n2UESuzjAORbGIlFffqXaoxN24U"
}
#############

app = FastAPI()


# app.mount("/static", StaticFiles(directory="../front/dist/front/browser"), name="static")



# url = "https://api.themoviedb.org/3/authentication"
# url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&with_genres=16"
url_genres = "https://api.themoviedb.org/3/genre/movie/list?language=en"

response_genres = requests.get(url_genres, headers=headers)
genres = response_genres.json().get("genres", [])


# def get_genre_id(genre_name):
#     """
#     Transforme le nom d'un genre en son Id
#     genre_name : String du nom du genre
#     """
#     for genre in genres:
#         if genre["name"].lower() == genre_name.lower():
#             return genre["id"]
#     return None

# def get_db_connection():
#     """Crée et retourne une connexion à la base de données PostgreSQL."""
#     try:
#         connection = psycopg2.connect(**DB_CONFIG)
#         return connection
#     except Exception as e:
#         print(f"Erreur de connexion à la base de données : {e}")
#         return None
    

# # Endpoint pour enregistrer un utilisateur
# @app.post("/register")
# def register(user: UserBaseModel):
#     username = user.username
#     email = user.email
#     password = user.password

#     if not username or not email or not password:
#         raise HTTPException(status_code=400, detail="Tous les champs sont requis")

#     connection = get_db_connection()
#     if not connection:
#         raise HTTPException(status_code=500, detail="Erreur de connexion à la base de données")

#     try:
#         with connection.cursor() as cursor:
#             query = sql.SQL("""
#                 INSERT INTO "User" (username, email, password)
#                 VALUES (%s, %s, %s) RETURNING id, username, email;
#             """)
#             cursor.execute(query, (username, email, password))
#             connection.commit()
#             user = cursor.fetchone()

#             return {"message": "Utilisateur créé", "user": {"id": user[0], "username": user[1], "email": user[2]}}

#     except Exception as e:
#         print(f"Erreur lors de l'insertion : {e}")
#         raise HTTPException(status_code=500, detail="Erreur serveur")
#     finally:
#         connection.close()




# # Est ce qu'on considere le cas ou les 3 ont des gouts différents ? 
# # Ma vision c'est on regarde les genres et en fonction de si au moins 50% aiment ce genre, on va pouvoir proposer des films avec ce genre.
# @app.get("/")
# def read_root():
#     genre_id = get_genre_id("History")
#     url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&with_genres={genre_id}"
#     response = requests.get(url, headers=headers)
#     return {"message": "Hello, World!", "request_genre": response.json()}


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# # a refaire
# # On va recup les utilisateurs
# # on va faire la somme des preferences 
# # trouver les ids avec + de 50% 
# # avec la string totale 
# # faire la requete 

# @app.get("/find/movies")
# def find_movie_with_genres():
#     genre_id = get_genre_id("History")
#     url = f"https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&with_genres={genre_id}"
#     response = requests.get(url, headers=headers)
#     return {"message": "Hello, World!", "request_genre": response.json()}


# # Mauvaise technique, il faut faire tourner le serveur front et le server backend differemment
# @app.get("/test")
# def serve_spa():
#     return FileResponse(os.path.join("../front/dist/front/browser", "index.html"))


# # utiliser logger pour ajouter les logs dans le sql 