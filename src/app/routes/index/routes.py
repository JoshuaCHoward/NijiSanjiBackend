from __future__ import annotations

from typing import Dict

from fastapi import APIRouter

import src.app.routes.index as index

router = APIRouter()


@router.get(index.enums.Routes.INDEX)
async def index() -> Dict[str, str]:
    return {
        "info": "This is the index page of fastapi-nano. "
                "You probably want to go to 'http://<hostname:port>/docs'.",
    }
