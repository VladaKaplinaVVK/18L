from flask import request, make_response
from flask_restx import Resource, Namespace
from dao.model.movies import MovieSchema

from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        schema = MovieSchema(many=True)
        movies = schema.dump(movies_service.get_movies(**request.args))
        return movies, 200

    def post(self):
        new_movie = movies_service.create_movie(request.json)
        resp = make_response("", 201)
        resp.header['location'] = f"{movie_ns.path}/{new_movie.id}"
        return resp


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        schema = MovieSchema(many=True)
        return schema.dump(movies_service.get_movies(movie_id)), 200

    def patch(self, movie_id: int):
        schema = MovieSchema(many=True)
        return schema.dump(movies_service.partial_update(movie_id, request.json)), 200

    def put(self, movie_id: int):
        schema = MovieSchema(many=True)
        return schema.dump(movies_service.update_all(movie_id, request.json)), 200

    def delete(self, movie_id: int):
        movies_service.delete(movie_id)
        return "", 204




