import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.config import FROM_EMAIL, FROM_PASSWORD


def send_email(subject, body, to_emails):
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

