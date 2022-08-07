from flask import Blueprint

rc = Blueprint('receitas', __name__)
dp = Blueprint('despesas', __name__)


from . import receitas, despesas

