import requests
from src.config.settings import url1, params1, NEWS_API_KEY

def buscar_noticias1():
    try:
        response = requests.get(url1, params={**params1, "apiKey": NEWS_API_KEY}, timeout=20)
        if response.status_code == 200:
            dados = response.json()
            artigos = dados.get("articles", [])
            noticias_formatadas = "\n\n".join(f"Título: {a['title']}\nDescrição: {a['description']}\nFonte: {a['url']}"
                                      for a in artigos)
            return noticias_formatadas
        else:
            print("STATUS CODE:", response.status_code)
            print("RESPOSTA COMPLETA:")
            print(response.json())
    except Exception as e:
        print("Erro:", e)