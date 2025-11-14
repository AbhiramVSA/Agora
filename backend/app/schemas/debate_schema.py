from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.debate_model import (
	DebateMode,
	DebateStatus,
	MessageType,
	ParticipantRole,
	SenderType,
)
from .agent_schema import AgentSummary
from .baseUUIDschema import BaseUUIDSchema
from .user_schema import UserSummary


class DebateBase(BaseModel):
	topic: str = Field(min_length=3, max_length=255)
	description: Optional[str] = Field(default=None, max_length=4000)
	mode: DebateMode = DebateMode.CHAT
	agent_id: Optional[UUID] = None
	topic_tags: Optional[list[str]] = None
	allow_spectators: bool = False

	model_config = ConfigDict(from_attributes=True)


class DebateCreate(DebateBase):
	created_by_id: UUID
	status: DebateStatus = DebateStatus.DRAFT
	scheduled_for: Optional[datetime] = Field(default=None)


class DebateUpdate(BaseModel):
	topic: Optional[str] = Field(default=None, min_length=3, max_length=255)
	description: Optional[str] = Field(default=None, max_length=4000)
	mode: Optional[DebateMode] = None
	status: Optional[DebateStatus] = None
	topic_tags: Optional[list[str]] = None
	agent_id: Optional[UUID] = None
	allow_spectators: Optional[bool] = None
	started_at: Optional[datetime] = None
	ended_at: Optional[datetime] = None

	model_config = ConfigDict(from_attributes=True)


class DebateRead(DebateBase, BaseUUIDSchema):
	status: DebateStatus
	created_by_id: UUID
	started_at: Optional[datetime] = None
	ended_at: Optional[datetime] = None


class DebateDetail(DebateRead):
	created_by: Optional[UserSummary] = None
	agent: Optional[AgentSummary] = None


class DebateParticipantBase(BaseModel):
	debate_id: UUID
	role: ParticipantRole
	user_id: Optional[UUID] = None
	agent_id: Optional[UUID] = None
	is_active: bool = True

	model_config = ConfigDict(from_attributes=True)


class DebateParticipantCreate(DebateParticipantBase):
	pass


class DebateParticipantRead(DebateParticipantBase, BaseUUIDSchema):
	joined_at: datetime


class DebateMessageBase(BaseModel):
	debate_id: UUID
	content: str
	sender_type: SenderType
	message_type: MessageType = MessageType.CHAT
	participant_id: Optional[UUID] = None
	agent_id: Optional[UUID] = None
	turn_index: Optional[int] = None
	payload: Optional[dict] = None

	model_config = ConfigDict(from_attributes=True)


class DebateMessageCreate(DebateMessageBase):
	pass


class DebateMessageRead(DebateMessageBase, BaseUUIDSchema):
	sent_at: datetime
