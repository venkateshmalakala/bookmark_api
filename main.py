from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException, status
from sqlmodel import Field, Session, SQLModel, create_engine, select

# --- DATABASE SETUP ---
sqlite_file_name = "bookmarks.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url)

# --- DATA MODEL ---
class Bookmark(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str
    title: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# --- APP SETUP ---
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- ENDPOINTS ---

# 1. Create Bookmark
@app.post("/bookmarks", response_model=Bookmark, status_code=status.HTTP_201_CREATED)
def create_bookmark(bookmark: Bookmark):
    if not bookmark.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    if not (bookmark.url.startswith("http://") or bookmark.url.startswith("https://")):
         raise HTTPException(status_code=400, detail="Invalid URL format")

    with Session(engine) as session:
        session.add(bookmark)
        session.commit()
        session.refresh(bookmark)
        return bookmark

# 2. Get All Bookmarks
@app.get("/bookmarks", response_model=List[Bookmark], status_code=status.HTTP_200_OK)
def read_bookmarks():
    with Session(engine) as session:
        bookmarks = session.exec(select(Bookmark)).all()
        return bookmarks

# 3. Get Single Bookmark
@app.get("/bookmarks/{id}", response_model=Bookmark, status_code=status.HTTP_200_OK)
def read_bookmark(id: int):
    with Session(engine) as session:
        bookmark = session.get(Bookmark, id)
        if not bookmark:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        return bookmark

# 4. Update Bookmark
@app.put("/bookmarks/{id}", response_model=Bookmark, status_code=status.HTTP_200_OK)
def update_bookmark(id: int, bookmark_update: Bookmark):
    # --- ADDED VALIDATION HERE ---
    if not bookmark_update.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    if not (bookmark_update.url.startswith("http://") or bookmark_update.url.startswith("https://")):
         raise HTTPException(status_code=400, detail="Invalid URL format")
    # -----------------------------

    with Session(engine) as session:
        db_bookmark = session.get(Bookmark, id)
        if not db_bookmark:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        
        db_bookmark.url = bookmark_update.url
        db_bookmark.title = bookmark_update.title
        db_bookmark.description = bookmark_update.description
        
        session.add(db_bookmark)
        session.commit()
        session.refresh(db_bookmark)
        return db_bookmark

# 5. Delete Bookmark
@app.delete("/bookmarks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bookmark(id: int):
    with Session(engine) as session:
        bookmark = session.get(Bookmark, id)
        if not bookmark:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        
        session.delete(bookmark)
        session.commit()
        return None