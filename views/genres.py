from flask_restx import Resource, Namespace
from dao.model.genres import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        schema = GenreSchema(many=True)
        genres = schema.dump(genre_service.get_genres())
        return genres, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    schema = GenreSchema(many=True)

    def get(self, gid: int):
        return self.schema.dump(genre_service.get_genres(gid)), 200
