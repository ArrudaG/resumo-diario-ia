import requests
from src.config.settings import GNEWS_API_KEY, url2, params2

def buscar_noticias2():
    try:
        response = requests.get(url2, params={**params2, "apikey": GNEWS_API_KEY}, timeout=20)
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
        print("ERRO: ", e)