from fastapi import APIRouter, HTTPException
from .mocks import fake_gameList, factorio_versions


info_router = APIRouter(
    prefix="/api/v1/info",
    tags=["Info"],
    # For later use maybe?
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@info_router.get("/List_installed-games")
async def supported_game_list():
    # todo find a way to list currently installed games
    #  will be do for puting in the db
    #  and displaying in a ui daya to return
    #  list of?
    #  instance_name | game_name-version?
    return " currently not supported "
# todo need away to get the current running game_control and version


@info_router.get("/game_support_list")
async def supported_game_list():
    # fixme this should be a sql server call once we have an sql server
    # data in db will look like gameUUDI | gameName
    games = fake_gameList
    if games:
        # todo set up a db with a list of versions for a few games for testing
        return games
    else:
        raise HTTPException(status_code=404, detail="no game_control name provided")


@info_router.get("/supported-game-versions")
async def supported_game_list(game_name=None):
    if game_name == "factorio":
        # todo set up a db with a list of versions for a few games for testing
        return await factorio_versions()
    else:
        raise HTTPException(status_code=404, detail="game_control not found")
