from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models.content import Content, User
from app.schemas.content import ContentCreate, ContentUpdate, ContentOut
from typing import List

router = APIRouter(prefix="/content", tags=["content"])

@router.post("/", response_model=ContentOut, status_code=201)
def create_content(
    payload: ContentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if db.query(Content).filter(Content.slug == payload.slug).first():
        raise HTTPException(status_code=409, detail="Slug already exists")

    post = Content(**payload.model_dump(), author_id=current_user.id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.get("/", response_model=List[ContentOut])
def list_content(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return db.query(Content).offset(skip).limit(limit).all()

@router.get("/{slug}", response_model=ContentOut)
def get_content(slug: str, db: Session = Depends(get_db)):
    post = db.query(Content).filter(Content.slug == slug).first()
    if not post:
        raise HTTPException(status_code=404, detail="Content not found")
    return post

@router.patch("/{post_id}", response_model=ContentOut)
def update_content(
    post_id: int,
    payload: ContentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    post = db.query(Content).filter(Content.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Content not found")
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your content")

    update_data = payload.model_dump(exclude_unset=True)  # only patch provided fields
    for key, value in update_data.items():
        setattr(post, key, value)

    db.commit()
    db.refresh(post)
    return post

@router.delete("/{post_id}", status_code=204)
def delete_content(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    post = db.query(Content).filter(Content.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Content not found")
    if post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your content")

    db.delete(post)
    db.commit()