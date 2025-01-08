from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..hashing import Hash

def create(request: schemas.User, db: Session):
    new_user = models.User(first_name=request.FirstName, last_name=request.LastName,
                           user_name=request.UserName, email=request.Email,
                           password=Hash.bcrypt(request.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"User with the id {id} is not available")
    return user

def update_user(id: int, user_update: schemas.UserUpdateRequest, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail=f"user with id: {id} does not exists")

    if user_update.first_name is not None:
        user.first_name = user_update.first_name
    if user_update.last_name is not None:
        user.last_name = user_update.last_name
    if user_update.roles is not None:
        user.roles = user_update.roles

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
