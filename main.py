import subprocess

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"User": "not-root"}


@app.put("/install-game")
async def game_in_stall(game: str, version: str, user: str, group: str):
    try:
        subprocess.call("blah.sh")
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled


@app.get("/supported-games")
async def supported_game_list():
    # todo set up a db a few games for testing
    text = ["Factorio"]

    return text


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
