
import logging
import sys

from flask import Flask, jsonify, make_response, render_template, request
from flask_mail import Mail
from flask_restx import Api, Resource, fields
from sqlalchemy_utils import create_database, database_exists

from controllers import FeedbackController
from models.feedback import db

#mail = Mail(app)


app = Flask(__name__)
app.config.from_pyfile('utils\config.py')
api = Api(app)
db.init_app(app)
feedback_controller = FeedbackController(db)

if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])
with app.app_context():
    db.create_all()

feedback_model = api.model('FeedBackModel', {
    'id': fields.String,
    'feedback': fields.String,
})

@api.route('/feedbacks')
class FeedbackList(Resource):
    @api.expect(feedback_model)
    def post(self):
        return feedback_controller.catch_feedback(request)

@api.route('/report')
class Report(Resource):
    def get(self):
        """
        Renderiza o template HTML para o relatório de feedback.
        Retorna o HTML do relatório.
        """
        feedbacks, positive_percentage, sorted_features = feedback_controller.generate_all_feedbacks_report()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('report.html', feedbacks=feedbacks, positive_percentage=positive_percentage, sorted_features=sorted_features),200,headers)

if __name__ == "__main__":
    #logging.info(f"Application started at port {5000}")
    #app.run(debug= '--debug' in sys.argv, port = PORT, host= DEPLOY_URL)
    logging.info(f"Application started at port {5000}")
    app.run(debug= '--debug' in sys.argv, port = 5000, host= "0.0.0.0")
