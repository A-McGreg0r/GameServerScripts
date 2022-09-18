import subprocess
from uuid import UUID
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Internal imports

# note fake user is only for testing the auth api should take care of tokens for the over all service
from fake_login import fake_users_db, UserInDB, fake_hash_password, get_current_active_user, User

app = FastAPI()


# idea all api are going to need an audit log so we can see what command are ran and so on (do this once it works)
# versions will be stored under a diffrent table and use the games uuid to get a list of versions.
# a temp table for testing


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# idea the auth suff hear should only be for local user and testing
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


# idea the auth suff hear should only be for local user and testing
@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


# control api are for admin only
# todo integrate the create user service and install scripts
@app.post("/api/v1/initialize/install-game")
async def game_install(game: str, version: str, user: UUID, ):
    try:
        subprocess.run("app/scripts/shell/linux/initialize/createUser.sh")
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled


@app.post("/api/v1/control/update-game")
async def game_install(game: str, version: str, user: UUID, ):
    try:
        return "end point currently unsupported"
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled


@app.post("/api/v1/control/uninstall-game")
async def game_install(game: str, user: str, ):
    try:
        subprocess.call("blah.sh")
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled


@app.get("/api/v1/info/test", tags=["info"])
async def some_test():
    return "test"
