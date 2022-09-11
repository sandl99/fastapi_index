from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_base
import databases

from backend import app

import backend

database = databases.Database(backend.DATABASE_URL)
Base = declarative_base()


class IndexTest(Base):
    __tablename__ = 'index_test_tab'

    id = Column(Integer, primary_key=True)
    ctime = Column(DateTime, index=True, nullable=False)
    utime = Column(DateTime, nullable=False)


@app.on_event("start_up")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


