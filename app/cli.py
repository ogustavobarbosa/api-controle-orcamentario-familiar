import click
from .models import db


def cria_db():
    db.create_all()


def init_app(app):
    for comando in [cria_db, ]:
        app.cli.add_command(app.cli.command()(comando))
