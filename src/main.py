from datetime import datetime
from src.services.email_service import enviar_email
from src.services.reports_service import salvar_report
from src.services.newsapi_service import buscar_noticias1
from src.services.gnewsapi_service import buscar_noticias2
from src.services.ia_service import gerar_resumo

def main():
    try:
        noticias1 = buscar_noticias1()
        noticias2 = buscar_noticias2()
        if noticias1 and noticias2:
            resumo = gerar_resumo(noticias1, noticias2)
            salvar_report(resumo)
            enviar_email(f"Resumo semanal: {datetime.now():%d/%m/%Y}", f"{resumo}")
        else:
            print("Nenhuma notícia encontrada")
    except Exception as e:
        print("Erro:",e)

if __name__ == "__main__":
    main()