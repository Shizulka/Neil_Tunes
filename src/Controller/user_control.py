from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.Infrastructure.database import get_db 
from src.Service.user_service import SongService


router = APIRouter()

@router.post("/create")
def create_song  ( name : str , album: str , release_date: str , db: Session = Depends(get_db)):
    service = SongService(db)
    song = service.create_song(name=name, album=album, release_date=release_date)

    if not song:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail="Song already exists"
        )
    return { "name": song.name , "album" : song.album , "release_date" :  song.release_date }

