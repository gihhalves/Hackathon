from fastapi import APIRouter, Header, HTTPException
from sqlalchemy.orm import Session

from services.execution_service import execute_script
from core.config import API_TOKEN
from core.database import SessionLocal

from models.log_model import ExecutionLog

router = APIRouter()

@router.post("/execute/{script_name}")
def run_script(script_name: str, x_isy_token: str = Header(None)):

    if x_isy_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")

    result = execute_script(script_name)

    db: Session = SessionLocal()

    log = ExecutionLog(
        script_name=script_name,
        status="success" if result["returncode"] == 0 else "error",
        output=result["stdout"] or result["stderr"]
    )

    db.add(log)
    db.commit()

    return result