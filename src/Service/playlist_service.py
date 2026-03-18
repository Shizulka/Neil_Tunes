from src.Infrastructure.models import Playlist
from src.Repository.playlist_repo import PlaylistRepository

class PlaylistService:
    def __init__(self, db):
        self.repository = PlaylistRepository(db)


    def create_playlist (self ,  name : str , ispublic: bool ):
        new_playlist = Playlist (name=name , ispublic= ispublic , user_id = None)

        return self.repository.create(new_playlist)

