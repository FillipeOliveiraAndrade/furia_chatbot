from openai import OpenAI
from app.services.settings import OPENAI_API_KEY
from app.services.contextos.contexto_base import contexto_institucional
from app.services.contextos.contexto_partidas_completo import contexto_partidas
from app.services.contextos.contexto_noticias import contexto_noticias

client = OpenAI(api_key=OPENAI_API_KEY)

# Mapeia conversas por sessão fictícia
conversas = {}

def consultar_openai(pergunta: str, session_id: str = "default") -> str:
    # Prompt refinado
    contexto = (
        contexto_institucional.strip() + "\n\n"
        + contexto_partidas.strip() + "\n\n"
        + contexto_noticias.strip()
    )

    # Recupera ou inicia histórico
    historico = conversas.get(session_id, [])
    historico.append({"role": "user", "content": pergunta})

    # Garante que não passe de 20 mensagens (mantém as últimas)
    if len(historico) > 20:
        historico = historico[-20:]

    messages = [{"role": "system", "content": contexto}] + historico

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.6
        )
        resposta = response.choices[0].message.content.strip()
        historico.append({"role": "assistant", "content": resposta})
        conversas[session_id] = historico
        return resposta
    except Exception as e:
        print("Erro ao consultar OpenAI:", e)
        return f"(erro) {str(e)}"
