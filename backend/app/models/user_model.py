from typing import ClassVar
from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from BaseUUIDmodel import BaseUUIDModel


class UserBase(SQLModel):
	username: str
	email: EmailStr = Field(nullable = False)

class User(BaseUUIDModel, UserBase, table = True):
	__tablename__ =  "user"
	hashed_password:  str | None = Field(default=None, nullable=False, index=True)
 

