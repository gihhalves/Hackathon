from sqlalchemy import Column, Integer, String
from core.database import Base

class ExecutionLog(Base):
    __tablename__ = "execution_logs"

    id = Column(Integer, primary_key=True, index=True)
    script_name = Column(String)
    status = Column(String)
    output = Column(String)