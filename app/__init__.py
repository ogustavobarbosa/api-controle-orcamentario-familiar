from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping({
        'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:1234@localhost/controle_orcamento',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })

    from .models import db
    db.init_app(app)

    from .models import migrate
    migrate.init_app(app, db)

    from . import cli
    cli.init_app(app)

    from .controllers import rc, dp
    app.register_blueprint(rc, url_prefix='/receitas')
    app.register_blueprint(dp, url_prefix='/despesas')


    return app


