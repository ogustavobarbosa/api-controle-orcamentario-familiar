import datetime
from ..models import db, fs_mixin
from sqlalchemy import extract

class Despesa(db.Model, fs_mixin):
    query: db.Query
    __tablename__ = 'despesas'

    
    id =  db.Column(db.INTEGER, primary_key=True)
    descricao =  db.Column(db.TEXT, nullable=False)
    valor = db.Column(db.FLOAT, nullable=False)
    data = db.Column(db.DATETIME(timezone=True), default=datetime.datetime.now)

    __fs_exclude_serialize_fields__ = ['id']

    def __fs_verify__(self, create=False):
        if Despesa.query\
                .filter(
            extract('month', Despesa.data) == extract('month', self.data)
        )\
                .filter(Despesa.descricao == self.descricao).all():

            raise Exception(f"A despesa '{self.descricao}' já existe no mês {self.data.split('-')[1]}")

        return True

    def __repr__(self):
        return f'<Despesa {self.id} {self.descricao} {self.data}>'
