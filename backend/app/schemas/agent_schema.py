from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from .baseUUIDschema import BaseUUIDSchema


class AgentBase(BaseModel):
	name: str = Field(min_length=2, max_length=150)
	display_name: Optional[str] = Field(default=None, max_length=150)
	description: Optional[str] = Field(default=None, max_length=2000)
	system_prompt: Optional[str] = Field(default=None, max_length=4000)
	voice_id: Optional[str] = Field(default=None, max_length=120)
	is_active: bool = True

	model_config = ConfigDict(from_attributes=True)


class AgentCreate(AgentBase):
	pass


class AgentUpdate(BaseModel):
	name: Optional[str] = Field(default=None, min_length=2, max_length=150)
	display_name: Optional[str] = Field(default=None, max_length=150)
	description: Optional[str] = Field(default=None, max_length=2000)
	system_prompt: Optional[str] = Field(default=None, max_length=4000)
	voice_id: Optional[str] = Field(default=None, max_length=120)
	is_active: Optional[bool] = None

	model_config = ConfigDict(from_attributes=True)


class AgentRead(AgentBase, BaseUUIDSchema):
	pass


class AgentSummary(BaseModel):
	id: UUID
	name: str
	display_name: Optional[str] = None

	model_config = ConfigDict(from_attributes=True)
