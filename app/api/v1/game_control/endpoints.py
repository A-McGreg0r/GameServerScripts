import subprocess
from uuid import UUID

from fastapi import APIRouter, HTTPException



game_control_router = APIRouter(
    prefix="/game_control-control",
    tags=["Game Controls"],
    # For later use maybe?
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# idea
#  This name space if for controlling a individual game service
#  more than one copy of a game can be ran but on in parallel
#  each "game" will have it own id
#  db/data might look something like
#  instance_id | instance_name (user defined) | game_id(relates to a game name) | version_id(relates to a game version)
#  will a user need an oauth toke to activate theses?
#  it would be better to implement ^ once I have an authService and UI it probably good practice
#  also its' more than likely good practice even more so this api is going to be ran though a web GUI

# requirements
#  only one game can be booted on start at a time

@game_control_router.post("/{game_control}/auto-start/")
async def game_install(game: str, user: UUID, on_boot: bool):
    try:
        if game:
            subprocess.run(f"enable {game}.service")
    except HTTPException:
        return HTTPException(status_code=400, detail="No token provided")

    except Exception as e:
        return f"An exception occurred {e}"
    finally:
        print("log some error info")


# fixme game_control is not a good name atm but not yet architected how this will work exactly
@game_control_router.post("/{game_control}/start")
async def game_install(game: str, start: bool):
    try:
        return "not yet implemented"
    except Exception as e:
        return f"An exception occurred {e}"
    except HTTPException:
        return HTTPException(status_code=400, detail="No Jessica token provided")
    finally:
        print("log some info")


# fixme game_control is not a good name atm but not yet architected how this will work exactly
@game_control_router.post("/{game_control}/stop/")
async def game_install(game: str, start: bool):
    try:
        return "not yet implemented"
    except Exception as e:
        return f"An exception occurred {e}"
    except HTTPException:
        return HTTPException(status_code=400, detail="No Jessica token provided")
    finally:
        print("log some info")


# fixme game_control is not a good name atm but not yet architected how this will work exactly
@game_control_router.put("/{game_control}/upload-save/",
                          summary="upload a save file",
                          description="upload a save for the game?",
                          )
async def game_install(game: str, start: bool):
    try:
        return "not yet implemented"
    except Exception as e:
        return f"An exception occurred {e}"
    except HTTPException:
        return HTTPException(status_code=400, detail="No Jessica token provided")
    finally:
        print("log some info")


# fixme game_control is not a good name atm but not yet architected how this will work exactly
@game_control_router.get("/{game_control}/download-save/")
async def game_install(game: str, start: bool):
    try:
        return "not yet implemented"
    except Exception as e:
        return f"An exception occurred {e}"
    except HTTPException:
        return HTTPException(status_code=400, detail="No Jessica token provided")
    finally:
        print("log some info")


# fixme game_control is not a good name atm but not yet architected how this will work exactly
@game_control_router.put("/{game_control}/upload-mod/")
async def game_install(game: str, start: bool):
    try:
        return "not yet implemented"
    except Exception as e:
        return f"An exception occurred {e}"
    except HTTPException:
        return HTTPException(status_code=400, detail="No Jessica token provided")
    finally:
        print("log some info")
