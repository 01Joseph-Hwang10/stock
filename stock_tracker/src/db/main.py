from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app: Flask) -> None:
    global db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db'
    db.init_app(app)

def get_db() -> SQLAlchemy:
    return db
