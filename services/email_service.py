import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.config import FROM_EMAIL, FROM_PASSWORD


def send_email(subject, body, to_emails):
    """
    Envia um email para os endereços de email especificados.

    Parâmetros:
    - subject (str): O assunto do email.
    - body (str): O corpo do email.
    - to_emails (list): Uma lista de endereços de email para os quais o email será enviado.

    Retorna:
    Nenhum valor de retorno.
    """
    from_email = FROM_EMAIL
    from_password = FROM_PASSWORD

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_emails, msg.as_string())
    server.quit()

