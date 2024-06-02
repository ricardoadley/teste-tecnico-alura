
import json

from flask import Response, jsonify

from models.feedback import Feedback
from services.feedback_service import analyze_feedback, generate_report


class FeedbackController:
    def __init__(self, db):
        self.db = db

    def catch_feedback(self, request):
            """
            Recebe um objeto de requisição e processa o feedback fornecido.

            Parâmetros:
            - request: Objeto de requisição contendo o feedback a ser processado.

            Retorna:
            - O resultado do processamento do feedback.
            """
            
            if not request.is_json:
                return json.dumps({"error": "Request body must be JSON"}), 400
            
            data = request.get_json()
            feedback_id = data.get('id')
            feedback_text = data.get('feedback')

            if feedback_text is None:
                return json.dumps({"error": "Feedback text is required"}), 400
            
            sentiment, requested_features = analyze_feedback(feedback_text)
            feedback = Feedback(
                id=feedback_id,
                feedback_text=feedback_text,
                sentiment=sentiment,
                requested_features=requested_features
            )
            self.db.session.add(feedback)
            self.db.session.commit()
            response = {
                "id": feedback.id,  
                "sentiment": sentiment,
                "requested_features": requested_features
            }
            return Response(json.dumps(response), status=200, mimetype='application/json')
    def _get_feedbacks(self):
            """
            Retorna todos os feedbacks existentes.

            Returns:
                feedbacks (list): Uma lista contendo todos os feedbacks existentes.
            """
            feedbacks = Feedback.query.all()
            return feedbacks
    def generate_all_feedbacks_report(self):
        """
        Gera um relatório de todos os feedbacks.

        Retorna um relatório gerado com base nos feedbacks disponíveis.
        """
        feedbacks = self._get_feedbacks()
        return generate_report(feedbacks)
    def feedback_detail(self, feedback_id):
        """
        Retorna os detalhes de um feedback com base no ID fornecido.

        Parâmetros:
        - feedback_id (int): O ID do feedback a ser retornado.

        Retorna:
        - feedback (Feedback): O objeto Feedback correspondente ao ID fornecido.

        Caso o feedback não seja encontrado, retorna um JSON com uma mensagem de erro e o código de status 404.
        """
        feedback = Feedback.query.get(feedback_id)
        if feedback is None:
            return jsonify({"error": "Feedback not found"}), 404
        return feedback
