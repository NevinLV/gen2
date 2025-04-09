import uuid
from typing import Annotated
from typing import List
from typing import Literal
from typing import LiteralString

from fastapi import APIRouter
from fastapi import Security

from gen.generators import generate_code

router = APIRouter(
    tags=["Публичное API"],
)


@router.post("/generator/example/", summary="Создать генератор задачи по примеру")
async def create_gen_task_for_example(
    text: str,
):
    """
    Создать генератор задачи по примеру.
    """

    response =  generate_code(text)

    return response


@router.get("/generator/example/", summary="Создать генератор задачи по примеру")
async def check_gen_task_for_example(
):
    """
    Создать генератор задачи по примеру.
    """

    response = "task_text"

    return response
