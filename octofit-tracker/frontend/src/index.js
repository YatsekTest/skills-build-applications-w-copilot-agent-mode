
import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Установим переменную окружения для Codespace URL
if (!process.env.REACT_APP_CODESPACE_URL) {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME || '';
  const protocol = window.location.protocol;
  const host = codespaceName
    ? `${protocol}//${codespaceName}-8000.app.github.dev`
    : `${protocol}//localhost:8000`;
  process.env.REACT_APP_CODESPACE_URL = host;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
