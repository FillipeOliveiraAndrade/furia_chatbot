from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from app.services.openai_service import consultar_openai
from fastapi.responses import JSONResponse

router = APIRouter()

class Pergunta(BaseModel):
    pergunta: str

@router.post("/ask")
def fazer_pergunta(pergunta: Pergunta, request: Request):
    try:
        session_id = request.client.host
        resposta = consultar_openai(pergunta.pergunta, session_id=session_id)
        resposta_formatada = resposta.replace("\n", " ").strip()
        return JSONResponse(content={"resposta": resposta_formatada})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
