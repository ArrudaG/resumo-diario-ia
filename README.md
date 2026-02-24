# 📊 Resumo de um Analista Financeiro IA  — AI News Intelligence System

Aplicação em Python para coleta automatizada de notícias financeiras, geração de resumo inteligente utilizando IA e criação de relatório semanal consolidado.

O objetivo do projeto é demonstrar habilidades em integração com APIs externas, processamento de dados, automação de rotinas, organização de código e uso de modelos de IA generativa em aplicações reais.

---

## 🚀 Funcionalidades

- Coleta automatizada de notícias financeiras via NEWSAPI e da GNEWSAPI  
- Filtragem de conteúdo relevante por palavra-chave  
- Consolidação de múltiplas notícias em um único contexto  
- Geração de resumo inteligente utilizando a API do Gemini  
- Geração de relatório semanal
- Tratamento de exceções para maior robustez  
- Execução automatizada 1x ao dia  

---

## 🧱 Estrutura do projeto

```text
.
├── .github/workflows/
│ └── monitor.yml
├── src/
│ ├── config/
│ ├── services/
│ └── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Tecnologias

- Python  
- Requests (consumo de API HTTP)  
- Integração com API do Gemini  
- SMTP (envio de email)
- GitHub Actions  

---

## 🧠 Arquitetura da Solução

Fluxo do sistema:

1. Busca notícias financeiras do dia  
2. Limita quantidade para controle de custo e performance  
3. Consolida títulos e descrições  
4. Envia um único contexto para a IA  
5. Gera um resumo estratégico consolidado  
6. Salva relatório semanal

Essa abordagem reduz chamadas à API de IA, melhora performance e mantém o custo sob controle.

---

## ☁️ Execução automatizada

O sistema pode ser executado automaticamente via GitHub Actions com agendamento semanal:

```yaml
0 8 * * *
```

Isso permite a execução do sistema na nuvem sem necessidade de servidor dedicado.

---

## ▶️ Executar localmente

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar a main:

```bash
python src/main.py
```

Criar arquivo .env com:

```ini
NEWS_API_KEY=your_key
GNEWS_API_KEY=your_key
GEMINI_API_KEY=your_key
EMAIL_USER=your_email
EMAIL_PASSWORD=email_password
REPORT_EMAILS=list_emails
```
---

## 📚 Aprendizados

Este projeto envolveu:

- Estruturação profissional de projeto Python
- Consumo de APIs REST
- Paginação e controle de requisições
- Integração com IA generativa
- Engenharia de prompts
- Automação com GitHub Actions
- Tratamento de erros e logs
- Organização modular de código
- Otimização de custo de chamadas externas
****
