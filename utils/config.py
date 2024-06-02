import os

from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
GPT_API_KEY = os.getenv('GPT_API_KEY')
FROM_EMAIL = os.getenv('FROM_EMAIL')
FROM_PASSWORD = os.getenv('FROM_PASSWORD')
TO_EMAILS = os.getenv('TO_EMAILS').split(',')