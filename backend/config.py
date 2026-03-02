import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max request size

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
