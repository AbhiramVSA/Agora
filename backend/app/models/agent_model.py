from __future__ import annotations

from typing import Optional

from pydantic import EmailStr
from sqlalchemy import Column, String
from sqlmodel import Field, SQLModel

from .BaseUUIDmodel import BaseUUIDModel

class BaseDebateAgent(SQLModel):
    prompt: str 
    

class DebateAgent(SQLModel):
    agent: BaseDebateAgent
    