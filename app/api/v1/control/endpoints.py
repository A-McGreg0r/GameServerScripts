from .mocks import fake_gameList
from .modles import Game
from uuid import UUID

from fastapi import APIRouter, HTTPException
from uuid import uuid4

control_router = APIRouter(
    prefix="/api/v1/control",
    tags=["control"],
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
        versions = ["1.2.12"]
        return versions
    else:
        raise HTTPException(status_code=404, detail="no game name provided")


@control_router.get("/supported-game-versions")
async def supported_game_list(game_name=None):
    if game_name:
        # todo set up a db with a list of versions for a few games for testing
        versions = ["1.2.12"]
        return versions
    else:
        raise HTTPException(status_code=404, detail="no game name provided")


@control_router.post("/update-game")
async def game_install(game: str, version: str, user: UUID, ):
    try:
        return "end point currently unsupported"
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled


