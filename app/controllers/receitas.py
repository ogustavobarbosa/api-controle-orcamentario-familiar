from ..models import Receita
from ..controllers import rc


@rc.route('/<int:receita_id>', methods=['GET', 'PUT', 'DELETE'])
@rc.route('/', methods=['GET', 'POST'])
def receitas(receita_id=None):
    return Receita.fs_get_delete_put_post(receita_id)

