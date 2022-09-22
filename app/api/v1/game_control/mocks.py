# versions will be stored under a diffrent table and use the games uuid to get a list of versions.
# a temp table for testing
from typing import List
from uuid import uuid4

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
