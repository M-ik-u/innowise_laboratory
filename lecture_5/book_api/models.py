from datetime import datetime
from sqlalchemy import Column, String, Integer, CheckConstraint
from db import Base, engine


CURRENT_YEAR = datetime.now().year


class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    author = Column(String, nullable=False,index=True)
    year = Column(Integer,CheckConstraint(f"year >= 0 AND year <={CURRENT_YEAR}"), nullable=True,index=True)


Base.metadata.create_all(bind=engine)