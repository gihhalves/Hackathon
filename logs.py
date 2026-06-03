from fastapi import APIRouter
from core.database import SessionLocal
from models.log_model import ExecutionLog

router = APIRouter()

@router.get("/logs")
def get_logs():

    db = SessionLocal()

    logs = db.query(ExecutionLog).all()

    return logs