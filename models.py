from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine('sqlite:///images.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    date_uploaded = Column(DateTime, default=func.now())
    filename = Column(String)
    dicom_data = Column(String)

Base.metadata.create_all(engine)
