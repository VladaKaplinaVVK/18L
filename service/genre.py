from dao.genres import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_genres(self, gid: None):
        return self.dao.get(gid)

