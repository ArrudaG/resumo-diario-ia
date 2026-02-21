import smtplib
import logging
import markdown

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.config.settings import EMAIL_USER, EMAIL_PASSWORD, EMAIL_TO

def enviar_email(assunto, mensagem):
    if not EMAIL_USER or not EMAIL_PASSWORD or not EMAIL_TO:
        raise ValueError("Credenciais de email não carregadas")

    try:
        html_content = markdown.markdown(mensagem)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = assunto
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO

        part_text = MIMEText(mensagem, "plain", "utf-8")

        part_html = MIMEText(html_content, "html", "utf-8")

        msg.attach(part_text)
        msg.attach(part_html)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(
                EMAIL_USER,
                EMAIL_TO,
                msg.as_string()
            )
        logging.info("Email enviado com sucesso")

    except Exception as e:
        print("ERRO SMTP:", e)
        logging.error(f"Erro ao enviar o email: {e}")