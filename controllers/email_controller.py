import schedule

from services.email_service import send_email
from services.feedback_service import get_weekly_feedback_summary
from utils.config import TO_EMAILS


def send_weekly_feedback_summary():
    """
    Envia um resumo semanal dos feedbacks por e-mail.

    Esta função obtém o conteúdo do resumo semanal dos feedbacks chamando a função get_weekly_feedback_summary().
    Em seguida, envia um e-mail com o assunto "Resumo Semanal de Feedbacks" para os destinatários especificados em TO_EMAILS.
    """
    email_content = get_weekly_feedback_summary()
    subject = "Resumo Semanal de Feedbacks"
    to_emails = TO_EMAILS
    send_email(subject, email_content, to_emails)

schedule.every().sunday.at("23:59").do(send_weekly_feedback_summary)