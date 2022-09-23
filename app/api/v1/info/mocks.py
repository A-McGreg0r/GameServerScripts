# versions will be stored under a diffrent table and use the games uuid to get a list of versions.
# a temp table for testing
from typing import List
from uuid import uuid4
import requests

from .modles import Game


fake_gameList: List[Game] = [
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


# idea this will likly end up as part of a cron job on  a diffrent service along with other scripts to get version
#  lists of games
def factorio_versions():
    url = 'https://updater.factorio.com/get-available-versions'
    resp = requests.get(url=url)
    items = resp.json()["core-linux_headless64"]
    res = []
    for x in range(0, len(items) - 1):
        res.append(items[x]["from"])

    return res
