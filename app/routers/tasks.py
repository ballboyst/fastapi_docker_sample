from fastapi import APIRouter


router = APIRouter()


@router.get("task")
async def get_task():
    pass