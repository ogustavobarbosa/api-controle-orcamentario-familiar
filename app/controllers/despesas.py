from ..controllers import dp
from ..models import Despesa


@dp.route('/<int:despesa_id>', methods=['GET', 'PUT', 'DELETE'])
@dp.route('/', methods=['GET', 'POST'])
def despesas(despesa_id=None):
    return Despesa.fs_get_delete_put_post(despesa_id)
