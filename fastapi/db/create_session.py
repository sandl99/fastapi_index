from uuid import uuid4

from fastapi.db import set_session_context, reset_session_context, session


def create_session(func):
    async def _standalone_session(*args, **kwargs):
        session_id = str(uuid4())
        context = set_session_context(session_id=session_id)

        try:
            await func(*args, **kwargs)
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.remove()
            reset_session_context(context=context)

    return _standalone_session
