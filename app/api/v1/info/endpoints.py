from .mocks import fake_gameList
from .modles import Game

from fastapi import APIRouter, HTTPException
from uuid import uuid4

info_router = APIRouter(
    prefix="/api/v1/info",
    tags=["Info"],
    # For later use maybe?
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@info_router.get("/game_support_list")
async def supported_game_list():
    # fixme this should be a sql server call once we have an sql server
    # data in db will look like gameUUDI | gameName
    games = ["factorio", "foo", "bar"]
    if games:
        # todo set up a db with a list of versions for a few games for testing
        return games
    else:
        raise HTTPException(status_code=404, detail="no game name provided")


@info_router.get("/supported-game-versions")
async def supported_game_list(game_name=None):

    # fixme this should be a sql server call once we have an sql server
    # data in db will look like versionUUDI | gameUUDI | gameVersion
    # and will do a right? join based on teh gameName,  gameUUID and get a list of versions for the game
    if game_name:
        # todo set up a db with a list of versions for a few games for testing
        versions = ["1.2.12"]
        return versions
    else:
        raise HTTPException(status_code=404, detail="no game name provided")

# need away to get the current running game and version
