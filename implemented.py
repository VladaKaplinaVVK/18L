from setup_db import db
from dao.movies import MovieDAO
from service.movie import MovieService
from dao.genres import GenreDAO
from service.genre import GenreService
from dao.directors import DirectorDAO
from service.director import DirectorService


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)


genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)