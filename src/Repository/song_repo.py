from src.Infrastructure.models import Song
from src.Repository.ult_repo import UltRepository

class SongRepository(UltRepository):
    def __init__(self, db):
        super().__init__(db, Song)
