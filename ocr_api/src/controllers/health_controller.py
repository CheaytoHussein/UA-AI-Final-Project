from typing import Dict

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check() -> Dict[str, str]:
    return {"status": "running"}
