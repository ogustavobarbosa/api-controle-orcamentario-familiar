from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_serialize import FlaskSerialize

db = SQLAlchemy()
migrate = Migrate()

fs_mixin = FlaskSerialize(db)

from .Receita import Receita
from .Despesa import Despesa
