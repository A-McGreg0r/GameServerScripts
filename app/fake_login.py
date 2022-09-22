from uuid import uuid4

from pydantic import BaseModel
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# idea might need to keep this in for running the service locally until a better way can be found


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


# idea the auth suff hear should be for local user only and testing
fake_users_db = {
    "johndoe": {

        "username": "admin",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    }
}


class UserInDB(User):
    hashed_password: str


# idea the auth stuff hear should be for local user only and testing
def fake_hash_password(password: str):
    return "fakehashed" + password


# idea the auth stuff hear should be for local user only and testing
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


# idea the auth stuff hear should be for local user only and testing
def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


# idea the auth stuff hear should be for local user only and testing
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


# idea the auth stuff hear should be for local user only and testing
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
