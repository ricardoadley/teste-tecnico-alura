
import json

from flask import Response, jsonify

from models.feedback import Feedback
from services.feedback_service import analyze_feedback, generate_report


class FeedbackController:
    def __init__(self, db):
        self.db = db

    def catch_feedback(self, request):
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
        feedbacks = Feedback.query.all()
        return feedbacks
    def generate_all_feedbacks_report(self):
        feedbacks = self._get_feedbacks()
        return generate_report(feedbacks)
        