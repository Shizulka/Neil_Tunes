from datetime import  datetime

from src.Infrastructure.models import Song
from src.Repository.song_repo import SongRepository

class SongService:
    def __init__(self, db):
        self.repository = SongRepository(db)
    
    def create_song(self ,  name : str , album: str , release_date: str):
        date_obj = datetime.strptime(release_date, "%d.%m.%Y").date()

        new_song = Song ( name=name , album=album , release_date=date_obj , author_id=None)
        return self.repository.create(new_song)
    

    def edit_song (self , song_id : int ,  updates: dict):
        song= self.repository.db.query(Song).filter(Song.song_id == song_id).first()

        if not song:
            return None

        for field, value in updates.items():
            setattr(song, field, value)

        self.repository.db.commit()
        self.repository.db.refresh(song)

        return song

    def delete_song (self , song_id : int ):
        song= self.repository.db.query(Song).filter(Song.song_id == song_id).first()

        if not song:
            return None
        
        return self.repository.delete(song)