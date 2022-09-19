from pydantic import BaseModel
from uuid import UUID, uuid4


class Game(BaseModel):
    id: UUID = uuid4
    name: str
    group: str
    versions: list
