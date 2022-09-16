import subprocess
from typing import List
from uuid import uuid4
from fastapi import FastAPI, HTTPException

# Internal imports
from modles import Game

app = FastAPI()

# versions will be stored under a diffrent table and use the games uuid to get a list of versions.
db: List[Game] = [
    Game(id=uuid4(),
         name="factorio",
         group="userName",
         versions=["1", "2", "Latest"]),
    Game(id=uuid4(),
         name="bar",
         group="userName",
         versions=["Latest"]),
    Game(id=uuid4(),
         name="foo",
         group="userName",
         versions=["Latest"])]


@app.get("/")
async def root():
    return {"User": "not-root"}


@app.post("/install-game")
async def game_install(game: str, version: str, user: str, ):
    try:
        subprocess.call("blah.sh")
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled


@app.get("/api/v1/supported-games")
async def supported_game_list():
    # todo set up a real db a few games for testing
    return db


# intended for admin use only
@app.post("/api/v1/add-supported-game")
async def supported_game_list(game: str, version: str):
    # todo set up a real db a few games for testing
    new_game = Game(id=uuid4(),
                    name=game,
                    group="userName",
                    versions=[version])

    db.append(new_game)

    return {"id": new_game.id,
            "name": game,
            "group": new_game.group,
            "versions": new_game.versions}


@app.get("/supported-game-versions")
async def supported_game_list(game_name=None):
    if game_name:
        # todo set up a db with a list of versions for a few games for testing
        versions = ["1.2.12"]
        return versions
    else:
        raise HTTPException(status_code=404, detail="no game name provided")


@app.get("/install_game")
async def read_user_item(game: str, version: str, user: str, group: str):
    try:
        subprocess.call("blah.sh")
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled
