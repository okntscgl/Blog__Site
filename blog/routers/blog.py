from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from ..repository import blog_repository

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

get_db = database.get_db

@router.get("/", response_model=List[schemas.ShowBlog])
async def all(db: Session = Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db),
                      current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.create(request, db, user_name=current_user.user_name)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id: int, db: Session = Depends(get_db),
                  current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: schemas.BlogCreate, db: Session = Depends(get_db),
                 current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.update(id, request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
async def show(id: int, db: Session = Depends(get_db),
               current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.show(id, db)
