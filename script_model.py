from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Script(Base):

    __tablename__ = "scripts"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True)

    description = Column(String)

    active = Column(Boolean, default=True)
