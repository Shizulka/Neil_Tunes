from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from contextlib import asynccontextmanager
from src.Infrastructure.database import get_db, db_ping

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App starting...")
    yield
    print("App shutting down...")


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db_ping(db)
        return {"status": "ok", "message": "робе"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
    

@app.get("/")
def root():
    return {"message": "робе"}