from .mocks import fake_gameList
from .modles import Game
from fastapi import APIRouter, HTTPException
from uuid import uuid4

control_router = APIRouter(
    prefix="/api/v1/control",
    tags=["Controls"],
    # For later use maybe?
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)



@control_router.post("/add_game_support")
async def add_game_support(game: str, version: str):
    # todo set up a real db a few games for testing
    new_game = Game(id=uuid4(),
                    name=game,
                    group="userName",
                    versions=[version])
    fake_gameList.append(new_game)

    return {"id": new_game.id,
            "name": game,
            "group": new_game.group,
            "versions": new_game.versions}


@control_router.get("/game_support_list")
async def supported_game_list(game_name=None):
    if game_name:
        # todo set up a db with a list of versions for a few games for testing
        games = ["factorio", "foo", "bar"]
        return game_name
    else:
        raise HTTPException(status_code=404, detail="no game_control name provided")






