import uuid
from typing import Annotated
from typing import List
from typing import Literal
from typing import LiteralString

from fastapi import APIRouter
from fastapi import Security

router = APIRouter(
    tags=["Публичное API"],
)


idea_statuses: dict[str, LiteralString] = {
    "TOP": "1",
    "NEW": "1",
    "PLANNED": "2",
    "READY": "3",
    "REJECTED": "4",
    "DUPLICATE": "5",
    "EXISTS": "6",
}
