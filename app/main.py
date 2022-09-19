import subprocess

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from api.v1.info.endpoints import info_router
from api.v1.initialize.endpoints import initialize_router
from api.v1.control.endpoints import control_router

# Internal imports

# note fake user is only for testing the auth api should take care of tokens for the over all service
from fake_login import fake_users_db, UserInDB, fake_hash_password, get_current_active_user, User

app = FastAPI()
app.include_router(info_router)
app.include_router(initialize_router)
app.include_router(control_router)

# idea all api are going to need an audit log so we can see what command are ran and so on (do this once it works)
# versions will be stored under a diffrent table and use the games uuid to get a list of versions.
# a temp table for testing


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# idea the auth stuff hear should only be for local user and testing
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


# idea the auth stuff hear should only be for local user and testing
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user



