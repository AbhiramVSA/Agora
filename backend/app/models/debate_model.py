from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Optional, TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, Column, Enum as SAEnum, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlmodel import Field, Relationship

from .BaseUUIDmodel import BaseUUIDModel

if TYPE_CHECKING:
    from .agent_model import Agent
    from .user_model import User


class DebateMode(str, Enum):
	CHAT = "chat"
	CALL = "call"


class DebateStatus(str, Enum):
	DRAFT = "draft"
	ACTIVE = "active"
	ENDED = "ended"
	ARCHIVED = "archived"


class ParticipantRole(str, Enum):
	USER = "user"
	AGENT = "agent"
	MODERATOR = "moderator"


class SenderType(str, Enum):
	USER = "user"
	AGENT = "agent"
	SYSTEM = "system"


class MessageType(str, Enum):
	CHAT = "chat"
	TRANSCRIPT = "transcript"
	SYSTEM = "system"


class Debate(BaseUUIDModel, table=True):
	"""High-level debate session tying together the topic, agent and participants."""

	topic: str = Field(sa_column=Column(String(255), nullable=False))
	description: Optional[str] = Field(
		default=None,
		sa_column=Column(Text, nullable=True),
	)
	mode: DebateMode = Field(
		sa_column=Column(SAEnum(DebateMode, name="debate_mode"), nullable=False),
	)
	status: DebateStatus = Field(
		default=DebateStatus.DRAFT,
		sa_column=Column(
			SAEnum(DebateStatus, name="debate_status"),
			nullable=False,
			server_default=DebateStatus.DRAFT.value,
		),
	)
	topic_tags: Optional[list[str]] = Field(
		default=None,
		sa_column=Column(JSONB, nullable=True),
		description="Optional topic tags to assist search and filtering.",
	)
	created_by_id: UUID = Field(foreign_key="user.id", nullable=False, index=True)
	agent_id: Optional[UUID] = Field(
		default=None,
		foreign_key="agent.id",
		nullable=True,
		index=True,
	)
	started_at: Optional[datetime] = Field(default=None, nullable=True)
	ended_at: Optional[datetime] = Field(default=None, nullable=True)
	allow_spectators: bool = Field(
		default=False,
		sa_column=Column(Boolean, nullable=False, server_default="false"),
	)

	created_by: Optional["User"] = Relationship(back_populates="debates_created")
	agent: Optional["Agent"] = Relationship(back_populates="debates")
	participants: list["DebateParticipant"] = Relationship(back_populates="debate")
	messages: list["DebateMessage"] = Relationship(back_populates="debate")


class DebateParticipant(BaseUUIDModel, table=True):
	"""Join table linking users/agents to a debate."""

	debate_id: UUID = Field(foreign_key="debate.id", nullable=False, index=True)
	user_id: Optional[UUID] = Field(
		default=None,
		foreign_key="user.id",
		nullable=True,
		index=True,
	)
	agent_id: Optional[UUID] = Field(
		default=None,
		foreign_key="agent.id",
		nullable=True,
		index=True,
	)
	role: ParticipantRole = Field(
		sa_column=Column(
			SAEnum(ParticipantRole, name="debate_participant_role"),
			nullable=False,
		),
	)
	joined_at: datetime = Field(
		default_factory=lambda: datetime.now(timezone.utc),
		nullable=False,
	)
	is_active: bool = Field(
		default=True,
		sa_column=Column(Boolean, nullable=False, server_default="true"),
	)

	debate: "Debate" = Relationship(back_populates="participants")
	user: Optional["User"] = Relationship(back_populates="debate_participations")
	agent: Optional["Agent"] = Relationship(back_populates="debate_participations")
	messages: list["DebateMessage"] = Relationship(back_populates="participant")


class DebateMessage(BaseUUIDModel, table=True):
	"""Message exchanged during a debate session."""

	debate_id: UUID = Field(foreign_key="debate.id", nullable=False, index=True)
	participant_id: Optional[UUID] = Field(
		default=None,
		foreign_key="debate_participant.id",
		nullable=True,
		index=True,
	)
	agent_id: Optional[UUID] = Field(
		default=None,
		foreign_key="agent.id",
		nullable=True,
		index=True,
	)
	sender_type: SenderType = Field(
		sa_column=Column(
			SAEnum(SenderType, name="debate_message_sender_type"),
			nullable=False,
		),
	)
	message_type: MessageType = Field(
		default=MessageType.CHAT,
		sa_column=Column(
			SAEnum(MessageType, name="debate_message_type"),
			nullable=False,
			server_default=MessageType.CHAT.value,
		),
	)
	content: str = Field(sa_column=Column(Text, nullable=False))
	turn_index: Optional[int] = Field(default=None, nullable=True)
	payload: Optional[dict] = Field(
		default=None,
		sa_column=Column(JSONB, nullable=True),
		description="Model-specific metadata such as token counts or speech URLs.",
	)
	sent_at: datetime = Field(
		default_factory=lambda: datetime.now(timezone.utc),
		nullable=False,
	)

	debate: "Debate" = Relationship(back_populates="messages")
	participant: Optional["DebateParticipant"] = Relationship(back_populates="messages")
	agent: Optional["Agent"] = Relationship(back_populates="messages")
