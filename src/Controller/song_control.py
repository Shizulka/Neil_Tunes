from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.Infrastructure.database import get_db 
from src.Service.song_service import SongService


router = APIRouter()

@router.post("/create")
def create_song  ( name : str , album: str , release_date: str , db: Session = Depends(get_db)):
    service = SongService(db)
    song = service.create_song(name=name, album=album, release_date=release_date)

    return { "name": song.name , "album" : song.album , "release_date" :  song.release_date }

@router.post("/edit")
def edit_song(song_id: int, name: str = None, album: str = None, release_date: str = None, db: Session = Depends(get_db)):
    service = SongService(db)
    date_obj = datetime.strptime(release_date, "%d.%m.%Y").date()

    all_fields = {"name": name, "album": album, "release_date": date_obj}
    updates = {field_name: value for field_name, value in all_fields.items() if value is not None}

    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")

    updated_song = service.edit_song(song_id=song_id, updates=updates)

    if updated_song is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Song with id {song_id} not found"
        )

    return {"song_id": updated_song.song_id}


@router.post("/delete")
def delete_song (song_id : int ,  db: Session = Depends(get_db)):
    service = SongService(db)
    song = service.delete_song(song_id = song_id)

    if song is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Song with id {song_id} not found"
        )
    
    return {  "Was delete" : song.song_id }


