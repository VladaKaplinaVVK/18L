from dao.directors import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_directors(self, did: None):
        return self.dao.get(did)

