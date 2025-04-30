from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat

app = FastAPI(
    title="FURIA Valorant Chatbot API",
    version="0.1.0",
    description="API para fornecer dados e respostas do chatbot FURIA."
)

# Adiciona o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Registra as rotas
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
