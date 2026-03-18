
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.Infrastructure.database import get_db 
from src.Service.playlist_service import PlaylistService


router = APIRouter()

@router.post("/create_playlist")
def create_playlist (  name : str , ispublic: bool ,  db: Session = Depends(get_db)):
    service = PlaylistService(db)
    playlist = service.create_playlist(name=name,  ispublic= ispublic )

    ##ну тіп перевірку чи є юзер idk зробити нада але я чьот не вдупляю як виглядатиме юзер і автор

    return {  "name": playlist.name }