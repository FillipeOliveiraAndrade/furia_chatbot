# 🐾 FURIA Chatbot

Um projeto de chatbot interativo e temático da FURIA Esports, com foco no cenário de **Valorant**. Desenvolvido com **React + TypeScript** no frontend e **FastAPI** no backend, o bot simula uma conversa empolgada com torcedores, responde perguntas sobre o time e ainda pode ser atualizado com dados em tempo real no futuro.

![banner furia chatbot](./docs/furia-banner.png) <!-- substitua com seu caminho real -->

---

## 🔥 Demonstração

> 💬 Em construção... Link de deploy será adicionado em breve!

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
  - Start command: `uvicorn app.services.main:app --host 0.0.0.0 --port 8000`

### Frontend (Vercel ou Render)
- Build com `npm run build`
- Deploy via GitHub no Vercel ou Render
- Consome a URL do backend publicada

---

## 📌 Atualizações Futuras

- 🔁 Integração com a API do [vlr.gg](https://vlr.gg) para estatísticas em tempo real
- 🎮 Modo "Fan Trivia" para testar conhecimento dos usuários sobre a FURIA
- 🌍 Suporte multilíngue
- 📱 Versão mobile responsiva

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
