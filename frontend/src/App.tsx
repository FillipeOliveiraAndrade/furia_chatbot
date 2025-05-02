import { useState, useRef, useEffect } from 'react';
import './App.css';

import bg from './assets/furia-bg.png';
import logo from './assets/logo.png';

import { askQuestion } from './api/chatbot';

const App = () => {
  const [messages, setMessages] = useState<{ from: 'user' | 'bot'; text: string }[]>([]);
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  const sendMessage = async () => {
    if (!input.trim()) return;
  
    const userMsg: { from: 'user' | 'bot'; text: string } = { from: 'user', text: input };
    const loadingMsg: { from: 'user' | 'bot'; text: string } = { from: 'bot', text: 'Digitando...' };
  
    setMessages((prev) => [...prev, userMsg, loadingMsg]);
    setInput('');

    try {
      const { data } = await askQuestion(input);
  
      // Substitui o "Digitando..." pela resposta real
      setMessages((prev) => [
        ...prev.slice(0, -1),
        { from: 'bot', text: data.resposta }
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev.slice(0, -1),
        { from: 'bot', text: 'Algo deu errado 😢 Tenta de novo daqui a pouco.' }
      ]);
    }
  };
  

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="app" style={{ backgroundImage: `url(${bg})` }}>
      <img src={logo} alt='logo da furia' className='logo' /> 

      <div className="chatbox">
        <div className="header">Como posso ajudar?</div>

        <div className="messages">
          {messages.map((msg, idx) => (
            <div key={idx} className={`msg ${msg.from}`}>
              {msg.text}
            </div>

          ))}

          <div ref={messagesEndRef} />
        </div>

        <div className="input-row">
          <input
            className="chat-input"
            placeholder="Digite sua pergunta..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
          />

          <button onClick={sendMessage}>➤</button>
        </div>
      </div>
    </div>
  );
};

export default App;
