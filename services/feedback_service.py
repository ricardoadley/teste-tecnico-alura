import json

from openai import OpenAI

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
def analyze_feedback(feedback_text):
    client = OpenAI(
        api_key=GPT_API_KEY,
    )
    response = client.chat.completions.create(
        model= "gpt-3.5-turbo", # model = "deployment_name".
        temperature = 0.0,
        messages=[
            {"role": "system", "content": f"{PROMPT}"},
            {"role": "user", "content": f"{feedback_text}"}
        ]
    )
    
    analysis = response.choices[0].message.content.replace("\\", "").replace("\n", "").replace("\t","")
    response_in_json = json.loads(analysis)

    return response_in_json["sentiment"], response_in_json["requested_features"]
