import smtplib
import logging
import markdown
import os
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from src.config.settings import EMAIL_USER, EMAIL_PASSWORD

class EmailService:

    def __init__(self):
        emails = json.loads(os.environ["REPORT_EMAILS"])

        if not EMAIL_USER or not EMAIL_PASSWORD:
            raise ValueError("Credenciais de email não carregadas")

        if not emails:
            raise ValueError("Email do destinatário näo carregado")

        self.user = EMAIL_USER
        self.password = EMAIL_PASSWORD
        self.to = emails

    def enviar(self, mensagem):

        try:
            html_content = markdown.markdown(mensagem)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_USER, EMAIL_PASSWORD)

                for email in self.to:
                    msg = MIMEMultipart("alternative")
                    msg["Subject"] = f"Resumo semanal: {datetime.now():%d/%m/%Y}"
                    msg["From"] = self.user
                    msg["To"] = email

                    part_text = MIMEText(mensagem, "plain", "utf-8")
                    part_html = MIMEText(html_content, "html", "utf-8")

                    msg.attach(part_text)
                    msg.attach(part_html)

                    server.sendmail(
                        self.user,
                        email,
                        msg.as_string()
                    )
                    logging.info(f"Email enviado para {email}")

        except Exception as error:
            logging.error(f"Erro ao enviar o email: {error}")
            raise