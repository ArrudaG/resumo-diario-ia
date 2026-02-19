import requests

from src.config.settings import url, params, NEWS_API_KEY

def busca_financeiro():
    try:
        response = requests.get(url, params={**params, "apiKey": NEWS_API_KEY}, timeout=10)
        if response.status_code == 200:
            dados = response.json()
            artigos = dados.get("articles", [])
            noticias_formatadas = "\n\n".join(f"Título: {a['title']}\nDescrição: {a['description']}"
                                      for a in artigos)
            return noticias_formatadas
        else:
            print("STATUS CODE:", response.status_code)
            print("RESPOSTA COMPLETA:")
            print(response.json())
    except Exception as e:
        print("Erro:", e)
