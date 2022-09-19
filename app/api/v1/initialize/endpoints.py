import subprocess
from uuid import UUID,uuid4

from .mocks import fake_gameList
from .modles import Game
from fastapi import APIRouter


initialize_router = APIRouter(
    prefix="/api/v1/initialize",
    tags=["Initialize"],
    # For later use maybe?
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# control api are for admin only
# todo integrate the create user service and install scripts
@initialize_router.post("/install-game")
async def game_install(game: str, version: str, user: UUID, ):
    try:
        subprocess.run("app/scripts/shell/linux/initialize/createUser.sh")
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled
