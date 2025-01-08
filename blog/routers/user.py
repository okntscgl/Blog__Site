from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import user_repository

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

get_db = database.get_db

@router.post("/", response_model=schemas.ShowUser)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_repository.create(request, db)

@router.get("/{id}", response_model=schemas.ShowUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    return user_repository.show(id, db)

@router.patch("/{id}", response_model=schemas.UserUpdateRequest)
async def partial_update_user(id: int, request: schemas.UserUpdateRequest, db: Session = Depends(get_db)):
    return user_repository.update_user(id, request, db)