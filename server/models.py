from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///database.sqlite3", convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()

Base.query = db_session.query_property()


class Schedule(Base):
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start = Column(Date)
    end = Column(Date)
