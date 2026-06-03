from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import subprocess
import os

app = FastAPI(title="IsyShell API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

TOKEN = "isy-secret-token"

@app.get("/")
def home():
    return FileResponse("isyshell-dashboard.html")

@app.get("/scripts")
def listar_scripts():
    try:
        arquivos = os.listdir("scripts")
        scripts = [f for f in arquivos if f.endswith(".sh")]
        return [{"name": s} for s in scripts]
    except:
        return []

@app.post("/execute/{nome}")
def executar(nome: str, x_isy_token: str = Header(...)):
    if x_isy_token != TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")
    try:
        resultado = subprocess.run(
            ["bash", f"scripts/{nome}"],
            capture_output=True,
            text=True
        )
        return {
            "script": nome,
            "stdout": resultado.stdout,
            "stderr": resultado.stderr,
            "status": "sucesso" if resultado.returncode == 0 else "erro"
        }
    except Exception as e:
        return {"erro": str(e)}

@app.get("/logs")
def logs():
    return []