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


#@control_router.post("/add_game_support")
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
