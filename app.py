import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Create Flask app
app = Flask(__name__)
app.secret_key = "your-secret-key-here"
# Simple SQLite database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize database
db = SQLAlchemy(app)
# Import models and routes after app creation
from models import *
from routes import *
# Create database tables
with app.app_context():
    db.create_all()