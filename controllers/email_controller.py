import schedule

from services.email_service import send_email
from services.feedback_service import get_weekly_feedback_summary
from utils.config import TO_EMAILS


def send_weekly_feedback_summary():
    email_content = get_weekly_feedback_summary()
    subject = "Resumo Semanal de Feedbacks"
    to_emails = TO_EMAILS
    send_email(subject, email_content, to_emails)

schedule.every().sunday.at("23:59").do(send_weekly_feedback_summary)