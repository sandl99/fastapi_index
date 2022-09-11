from sqlalchemy import Column, Integer, DateTime

from fastapi.db import Base


class IndexTest(Base):
    __tablename__ = 'index_test_tab'

    id = Column(Integer, primary_key=True)
    ctime = Column(DateTime, index=True, nullable=False)
    utime = Column(DateTime, nullable=False)
