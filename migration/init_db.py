import sqlalchemy

import backend
from models import IndexTest

engine = sqlalchemy.create_engine(
    backend.DATABASE_URL, echo=True
)
IndexTest.metadata.create_all(engine)
