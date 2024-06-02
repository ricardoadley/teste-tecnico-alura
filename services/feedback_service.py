import json
from datetime import datetime, timedelta

from openai import OpenAI

from models.feedback import Feedback
from utils.config import GPT_API_KEY

PROMPT = """
Seu retorno deve ser um json no seguinte modelo:
"sentiment": ,
"requested_features": [
{
"code": ,
"reason": 
}
]
Os campos devem ser preenchidos seguindo o modelo abaixo:
"sentiment": "POSITIVO",
"requested_features": [
{
"code": "EDITAR_PERFIL",
"reason": "O usuário gostaria de realizar a edição do próprio perfil"
}
]
o campo sentiment pode ser “POSITIVO”, “NEGATIVO” ou “INCONCLUSIVO”.
O feedback é o seguinte: 
"""

PROMPT_EMAIL = """
Escreva um resumo semanal sobre os feedbacks.O resumo deve citar a quantidade de feedbacks positivos,
de feedbacks negativos e as Principais funcionalidades pedidas"
"""
def analyze_feedback(feedback_text):
    client = OpenAI(
        api_key=GPT_API_KEY,
    )
    response = client.chat.completions.create(
        model= "gpt-3.5-turbo", 
        temperature = 0.0,
        messages=[
            {"role": "system", "content": f"{PROMPT}"},
            {"role": "user", "content": f"{feedback_text}"}
        ]
    )
    
    analysis = response.choices[0].message.content.replace("\\", "").replace("\n", "").replace("\t","")
    response_in_json = json.loads(analysis)

    return response_in_json["sentiment"], response_in_json["requested_features"]

def generate_report(feedbacks):
    total_feedbacks = len(feedbacks)
    positive_feedbacks = [f for f in feedbacks if f.sentiment == "POSITIVO"]
    positive_percentage = len(positive_feedbacks) / total_feedbacks * 100 if total_feedbacks > 0 else 0

    feature_count = {}
    for feedback in feedbacks:
        if feedback.requested_features:
            for feature in feedback.requested_features:
                code = feature['code']
                if code in feature_count:
                    feature_count[code] += 1
                else:
                    feature_count[code] = 1

    sorted_features = sorted(feature_count.items(), key=lambda x: x[1], reverse=True)
    return feedbacks, positive_percentage, sorted_features

def _generate_email_content(sorted_features,positive_percentage,negative_percentage):
    features_text = "\n".join([f"{feature}: {count} requests" for feature, count in sorted_features])
    client = OpenAI(
        api_key=GPT_API_KEY,
    )
    content_to_email = {}
    content_to_email['features_text'] = features_text
    content_to_email['positive_percentage'] = positive_percentage
    content_to_email['negative_percentage'] = negative_percentage
    response = client.chat.completions.create(
        model= "gpt-3.5-turbo", 
        temperature = 0.0,
        messages=[
            {"role": "system", "content": f"{PROMPT}"},
            {"role": "user", "content": f"{content_to_email}"}
        ]
    )
    email_body = response.choices[0].text.strip()
    return email_body
def _generate_data_for_summary(feedbacks):
    total_feedbacks = len(feedbacks)
    positive_feedbacks = [f for f in feedbacks if f.sentiment == "POSITIVO"]
    negative_feedbacks = [f for f in feedbacks if f.sentiment == "NEGATIVO"]

    positive_percentage = len(positive_feedbacks) / total_feedbacks * 100 if total_feedbacks > 0 else 0
    negative_percentage = len(negative_feedbacks) / total_feedbacks * 100 if total_feedbacks > 0 else 0

    feature_count = {}
    for feedback in feedbacks:
        if feedback.requested_features:
            for feature in feedback.requested_features:
                code = feature['code']
                if code in feature_count:
                    feature_count[code] += 1
                else:
                    feature_count[code] = 1
    sorted_features = sorted(feature_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_features,positive_percentage,negative_percentage

def get_weekly_feedback_summary():
    now = datetime.now()
    start_of_week = now - timedelta(days=now.weekday())
    feedbacks = Feedback.query.filter(Feedback.timestamp >= start_of_week).all()
    sorted_features,positive_percentage,negative_percentage = _generate_data_for_summary(feedbacks)
    email_body = _generate_email_content(sorted_features,positive_percentage,negative_percentage)
    return email_body


