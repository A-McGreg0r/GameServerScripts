from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum


class User:
    id: UUID = uuid4

class Game(BaseModel):
    id: UUID = uuid4
    name: str
    group: str
    versions: list
