import subprocess
from uuid import UUID, uuid4

from .mocks import fake_gameList
from .modles import Game
from fastapi import APIRouter, HTTPException

initialize_router = APIRouter(
    prefix="/initialize",
    tags=["Initialize"],
    # For later use maybe?
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# control api are for admin only
# todo integrate the create user service and install scripts
@initialize_router.post("/install-game_control")
async def game_install(game: str, version: str, user: UUID, ):
    try:
        # step one create a use as a no login for the game_control to be run as useing the game_control as games "user"
        # and the UUID of the user as the group doing so alows us to have the users loacal user manage the services
        # and run the games
        subprocess.run(f"adduser --disabled-login --no-create-home --gecos {game} {user}")
        # step two download the game_control
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return HTTPException(status_code=400, detail="No Jessica token provided")
    finally:
        print("log some error info")


@initialize_router.post("/update-game{game_id}")
async def game_install(game_id: UUID, version: str, user: UUID, ):
    try:
        return "end point currently unsupported"
    except Exception as e:
        return f"An exception occurred {e}"
    except:
        return "something has gone wrong"  # todo set a default error message when unhandled
