import os

from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
model = "gemini-2.5-flash"
url1 = "https://newsapi.org/v2/everything"
url2 = 'https://gnews.io/api/v4/search?'
params1 = {
    "q": "(Ibovespa OR B3 OR IFIX OR fluxo estrangeiro OR Petrobras OR Vale OR Itau OR Banco do Brasil OR Bradesco OR WEG) AND (Selic OR IPCA OR inflação OR Copom OR Banco Central) AND (dólar OR câmbio OR real)",
    "language": "pt",
    "pageSize": 10
}
params2 = {
    "q": "(Ibovespa OR B3 OR Petrobras OR Banco Santander OR Ouro OR Itau OR CSN OR Banco Central OR inflação OR Vael OR Banco do Brasil OR Selic)",
    "lang": "pt",
    "country": "br",
    "page": 10,
}