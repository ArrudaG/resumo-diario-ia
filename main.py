from src.services.reports_service import salvar_report
from src.services.newsapi_service import buscar_noticias1
from src.services.gnewsapi_service import buscar_noticias2
from src.services.ia_service import gerar_resumo
from src.services.resumo_semanal import ResumoSemanalService
from src.services.email_service import EmailService

def main():

    resumo_semanal = ResumoSemanalService(
        newsapi_service=buscar_noticias1,
        gnewsapi_service=buscar_noticias2,
        ia_service=gerar_resumo,
        report_service=salvar_report,
        email_service=EmailService()
    )

    resumo_semanal.executar()

if __name__ == "__main__":
    main()