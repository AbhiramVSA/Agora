from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from sqlmodel import SQLModel, Session, create_engine

from core.config import Settings

engine = create_engine(
	Settings.SQLALCHEMY_DATABASE_URI,
	echo=False,
	pool_pre_ping=True,
)


def init_db() -> None:
	"""Create database tables for all SQLModel subclasses."""

	SQLModel.metadata.create_all(bind=engine)


def get_session() -> Iterator[Session]:
	"""FastAPI dependency that yields a database session."""

	with Session(engine) as session:
		yield session


@contextmanager
def session_scope() -> Iterator[Session]:
	"""Provide a transactional scope around a series of operations."""

	session = Session(engine)
	try:
		yield session
		session.commit()
	except Exception:
		session.rollback()
		raise
	finally:
		session.close()