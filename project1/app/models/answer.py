from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    request_id = Column(Integer, ForeignKey('requests.id'))
    created_at = Column(DateTime)
    validated = Column(Boolean)
    