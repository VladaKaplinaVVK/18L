from flask_restx import Resource, Namespace
from dao.model.directors import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    schema = DirectorSchema(many=True)

    def get(self):
        return self.schema.dump(director_service.get_directors()), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    schema = DirectorSchema(many=True)

    def get(self, did: int):
        return self.schema.dump(director_service.get_directors(did)), 200
