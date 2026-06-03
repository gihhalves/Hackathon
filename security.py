from fastapi import Header, HTTPException
import os

API_TOKEN = os.getenv("API_TOKEN")

def validate_token(x_isy_token: str = Header(...)):

    if x_isy_token != API_TOKEN:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )