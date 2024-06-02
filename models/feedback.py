from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Feedback(db.Model):
    id = db.Column(db.String, primary_key=True)
    feedback_text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.String, nullable=False)
    requested_features = db.Column(db.JSON)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
