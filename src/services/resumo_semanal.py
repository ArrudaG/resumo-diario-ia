class ResumoSemanalService():
    def __init__(self, newsapi_service, gnewsapi_service, ia_service, report_service, email_service):
        self.newsapi_service = newsapi_service
        self.gnewsapi_service = gnewsapi_service
        self.ia_service = ia_service
        self.report_service = report_service
        self.email_service = email_service

    def executar(self):
        try:

            noticias1 = self.newsapi_service()
            noticias2 = self.gnewsapi_service()

            if noticias1 and noticias2:

                resumo = self.ia_service(noticias1, noticias2)
                self.report_service(resumo)
                self.email_service.enviar(f"{resumo}")

            else:
                raise ValueError("Notícias näo encontradas")

        except (KeyError, IndexError) as e:
            print("Erro ao gerar resumo: ", e)

        except Exception as e:
            print("Erro:", e)