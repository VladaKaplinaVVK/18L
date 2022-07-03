from dao.model.movies import Movie
from dao.movies import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_movies(self, mid: None, **kwargs):
        return self.dao.get(mid, **kwargs)

    def create_movie(self, data):
        return self.dao.create(data)

    def update_all(self, data, movie_id):
        movie = self.get_movies(movie_id)

        movie.title = data["title"],
        movie.description = data["description"],
        movie.trailer = data["trailer"],
        movie.year = data["year"],
        movie.rating = data["rating"],
        movie.genre_id = data["genre_id"],
        movie.director_id = data["director_id"]
        self.dao.update(movie)
        return movie

    def partial_update(self, data, movie_id):
        movie = self.get_movies(movie_id)

        if 'title' in data:
            movie.title = data["title"]
        elif 'trailer' in data:
            movie.trailer = data["trailer"]
        elif 'year' in data:
            movie.year = data["year"]
        elif 'rating' in data:
            movie.rating = data["rating"]
        elif 'genre_id' in data:
            movie.genre_id = data["genre_id"]
        elif 'director_id' in data:
            movie.director_id = data["director_id"]

        self.dao.update(movie)
        return movie

    def delete(self, movie_id):
        self.dao.delete(movie_id)

