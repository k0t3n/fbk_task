from sqlalchemy.dialects import postgresql

from app.db import db


class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer(), primary_key=True)
    headers = db.Column(db.Unicode())
    body = db.Column(db.Unicode())
    ip = db.Column(postgresql.INET())
