import { api } from "../api";

export const askQuestion = (question: string) => api.post('/chat/ask', { pergunta: question });
