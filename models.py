from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
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

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'date_uploaded': self.date_uploaded,
            'filename': self.filename,
            'dicom_data': self.dicom_data,
        }

Base.metadata.create_all(engine)
