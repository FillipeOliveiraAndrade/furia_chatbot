# 🐾 FURIA Chatbot

Um projeto de chatbot interativo e temático da FURIA Esports, com foco no cenário de **Valorant**. Desenvolvido com **React + TypeScript** no frontend e **FastAPI** no backend, o bot simula uma conversa empolgada com torcedores, responde perguntas sobre o time e ainda pode ser atualizado com dados em tempo real no futuro.

![banner furia chatbot](./src/assets/furia-bg.png)

---

## 🔥 Demonstração

🟢 Acesse agora:

- 💻 **Frontend (Vercel):** [https://furia-chatbot-eta.vercel.app](https://furia-chatbot-eta.vercel.app)
- 🔙 **Backend (Render):** [https://furia-chatbot-kqy0.onrender.com](https://furia-chatbot-kqy0.onrender.com)

---

## 🧠 Objetivo

Criar uma experiência conversacional que represente a identidade da FURIA Esports — com linguagem jovem, divertida e informativa, respondendo sobre:
- Escalação do time de Valorant
- Histórico de jogos e campeonatos
- Notícias recentes
- Curiosidades e desempenho

---

## ⚙️ Tecnologias

### Frontend
- [React](https://reactjs.org/)
- [TypeScript](https://www.typescriptlang.org/)
- Estilização com CSS puro
- API: Axios
- ✅ **Totalmente responsivo** para mobile, tablet e desktop

### Backend
- [FastAPI](https://fastapi.tiangolo.com/)
- OpenAI API (GPT-4o)
- Estrutura REST com múltiplas rotas

---

## 🗂 Estrutura de Pastas

```bash
furia_chatbot/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   └── render.yaml
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── api/
│   │   └── App.tsx
│   ├── public/
│   ├── vercel.json
│   └── package.json
```

---

## 🧩 Funcionalidades

- 💬 Interface de chat interativa com background da FURIA
- 🤖 Respostas baseadas em contexto pré-definido (lineup, jogos, notícias)
- 🎉 Linguagem jovem e engajada
- 💡 Mensagem personalizada com nome do usuário (opcional)
- 🔁 Histórico de conversa mantido durante a sessão
- 🚀 Chamadas para seguir a FURIA nas redes sociais
- 🧪 Mock de loading enquanto a IA responde
- 📱 Responsividade completa em telas pequenas

---

## 🔌 Diagramas Técnicos

### Fluxo Geral da Aplicação
> _adicione aqui a imagem do fluxo_

### Diagrama de Pastas
> _adicione aqui a imagem da estrutura_

---

## 🚀 Deploy

### Backend (Render.com)
- Deploy automático via GitHub
- Arquivo `render.yaml` configurado com:
  - Root directory: `backend`
  - Build command: `pip install -r requirements.txt`
  - Start command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Frontend (Vercel)
- Root directory: `frontend`
- Build command: `npm run build`
- Output: `dist`
- Proxy configurado com `vercel.json` para `/api` → backend

---

## 📌 Atualizações Futuras

- 🔁 Integração com a API do [vlr.gg](https://vlr.gg) para estatísticas em tempo real
- 🎮 Modo "Fan Trivia" para testar conhecimento dos usuários sobre a FURIA
- 🌍 Suporte multilíngue
- 📱 Versão mobile responsiva ✅ **(já implementada!)**

---

## 👨‍💻 Autor

Feito com 💜 por [Fillipe Oliveira Andrade](https://github.com/FillipeOliveiraAndrade)

---

## 📸 Créditos

- Logo e elementos visuais: FURIA Esports (uso institucional sem fins comerciais)
- Backgrounds adaptados com IA e design manual
- Dados de campeonatos e lineups: vlr.gg e liquipedia.net

---

## 🐾 Bora torcer juntos?
Siga a FURIA nas redes:
- [Instagram](https://instagram.com/furia)
- [Twitter/X](https://twitter.com/furia)
- [Site Oficial](https://furia.gg)