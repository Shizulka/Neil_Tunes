from datetime import datetime

from src.Infrastructure.models import Song
from src.Repository.song_repo import SongRepository

class SongService:
    def __init__(self, db):
        self.repository = SongRepository(db)
    
    def create_song(self ,  name : str , album: str , release_date: str):
        date_obj = datetime.strptime(release_date, "%d.%m.%Y").date()
        existing_song = self.repository.db.query(Song).filter(Song.name == name).first()

        if  existing_song:
            return None 

        new_song = Song ( name=name , album=album , release_date=date_obj , author_id=None)
        return self.repository.create(new_song)