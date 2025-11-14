from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from .baseUUIDschema import BaseUUIDSchema


class UserBase(BaseModel):
	username: str = Field(min_length=3, max_length=150)
	email: EmailStr

	model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
	password: str = Field(min_length=8, max_length=255)
	display_name: Optional[str] = Field(default=None, max_length=150)


class UserUpdate(BaseModel):
	username: Optional[str] = Field(default=None, min_length=3, max_length=150)
	email: Optional[EmailStr] = None
	password: Optional[str] = Field(default=None, min_length=8, max_length=255)
	display_name: Optional[str] = Field(default=None, max_length=150)

	model_config = ConfigDict(from_attributes=True)


class UserRead(UserBase, BaseUUIDSchema):
	display_name: Optional[str] = None


class UserSummary(BaseModel):
	"""Minimal payload embedded in debate responses."""

	id: UUID
	username: str
	display_name: Optional[str] = None

	model_config = ConfigDict(from_attributes=True)
