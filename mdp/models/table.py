from typing import Optional, List

from sqlalchemy import Column, String, Integer, Index, select
from sqlalchemy.orm import relationship, Session

from mdp.db import provide_session
from mdp.models.base import Base
from mdp.models.column import MetaColumn


class MetaTable(Base):
    __tablename__ = 'meta_table'

    id = Column(Integer, primary_key=True)
    database = Column(String(length=50))
    schema = Column(String(length=50))
    name = Column(String(length=50))
    description = Column(String(length=100))
    owner = Column(String(length=50))
    update_frequency = Column(String(length=1))

    columns = relationship('MetaColumn', back_populates='table')

    __table_args__ = (
        Index('idx_meta_table', database, schema, name, unique=True),
        {'extend_existing': True}
    )

    def __init__(
            self,
            database: str,
            schema: str,
            name: str,
            description: Optional[str] = None,
            owner: Optional[str] = None,
            update_frequency: Optional[str] = None
    ):
        self.database = database
        self.schema = schema
        self.name = name
        self.description = description
        self.owner = owner
        self.update_frequency = update_frequency

        self.columns: Optional[List[MetaColumn]] = None

    @provide_session
    def get_columns(self, session: Session = None) -> List[MetaColumn]:
        stmt = select(MetaColumn).where(MetaColumn.table_id == self.id)
        result = session.execute(stmt)
        return result.all()

    @provide_session
    def get_column(self, column_id, session: Session = None) -> MetaColumn:
        stmt = select(MetaColumn).where(MetaColumn.table_id == self.id, MetaColumn.id == column_id)
        result = session.execute(stmt)
        return result.first()

    @provide_session
    def generate_ddl(self, session: Session = None) -> str:
        columns = self.get_columns(session=session)
        columns_string = [f'{col.name} {col.data_type}' for col in columns]
        sql = f'CREATE TABLE {self.database}.{self.schema}.{self.name} ({columns_string})'
        return sql
