from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from sqlalchemy import Boolean, Column, String, Text
from sqlmodel import Field, Relationship

from .BaseUUIDmodel import BaseUUIDModel

if TYPE_CHECKING:
    from .debate_model import Debate, DebateMessage, DebateParticipant


class Agent(BaseUUIDModel, table=True):
    """Customisable AI personas that can participate in debates."""

    name: str = Field(sa_column=Column(String(150), unique=True, nullable=False))
    display_name: Optional[str] = Field(
        default=None,
        sa_column=Column(String(150), nullable=True),
    )
    description: Optional[str] = Field(
        default=None,
        sa_column=Column(Text, nullable=True),
    )
    system_prompt: Optional[str] = Field(
        default=None,
        sa_column=Column(Text, nullable=True),
        description="Prompt injected as system message when composing AI responses.",
    )
    voice_id: Optional[str] = Field(
        default=None,
        sa_column=Column(String(120), nullable=True),
        description="Identifier of the TTS voice to use for call debates.",
    )
    is_active: bool = Field(
        default=True,
        sa_column=Column(Boolean, nullable=False, server_default="true"),
    )

    debates: list["Debate"] = Relationship(back_populates="agent")
    debate_participations: list["DebateParticipant"] = Relationship(
        back_populates="agent"
    )
    messages: list["DebateMessage"] = Relationship(back_populates="agent")
