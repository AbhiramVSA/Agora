from __future__ import annotations

from pydantic import BaseModel

class BaseContext(BaseModel):
    context: str 