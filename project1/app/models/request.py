from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    type = Column(String)
    created_at = Column(DateTime)
    status = Column(String)
    