from contextvars import ContextVar, Token

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session
from sqlalchemy.orm import declarative_base, sessionmaker

from fastapi import config

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


engine = create_async_engine(config.DATABASE_URL, pool_recycle=3600)
async_session_factory = sessionmaker(
    bind=engine,
    autocommit=True,
    autoflush=False,
    class_=AsyncSession,
)
session = async_scoped_session(async_session_factory, scopefunc=get_session_context)
Base = declarative_base()
