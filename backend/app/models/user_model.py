from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from pydantic import EmailStr
from sqlalchemy import Column, String
from sqlmodel import Field, Relationship, SQLModel

from .BaseUUIDmodel import BaseUUIDModel

if TYPE_CHECKING:
    from .debate_model import Debate, DebateParticipant


class UserBase(SQLModel):
    username: str = Field(sa_column=Column(String(150), unique=True, nullable=False))
    email: EmailStr = Field(sa_column=Column(String(255), unique=True, nullable=False))


class User(BaseUUIDModel, UserBase, table=True):
    hashed_password: str = Field(
        sa_column=Column(String(255), nullable=False),
        description="BCrypt or Argon2 hashed password.",
    )

    display_name: Optional[str] = Field(
        default=None,
        sa_column=Column(String(150), nullable=True),
    )

    debates_created: list["Debate"] = Relationship(back_populates="created_by")
    debate_participations: list["DebateParticipant"] = Relationship(
        back_populates="user"
    )












