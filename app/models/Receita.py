import datetime
from ..models import db, fs_mixin
from sqlalchemy  import extract

class Receita(fs_mixin, db.Model):
    query: db.Query
    __tablename__ = 'receitas'

    id = db.Column(db.INTEGER, primary_key=True)
    descricao = db.Column(db.TEXT, nullable=False)
    valor = db.Column(db.FLOAT, nullable=False)
    data =  db.Column(db.DATETIME(timezone=True), default=datetime.datetime.now)

    __fs_exclude_json_serialize_fields__ = ['id']


    def __fs_verify__(self, create=False):
        if Receita.query\
                .filter(
            extract('month', Receita.data) == extract('month', self.data)
        )\
                .filter(Receita.descricao == self.descricao).all():

            raise Exception(f"A despesa '{self.descricao}' já existe no mês {self.data.split('-')[1]}")

        return True




