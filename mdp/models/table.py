from typing import Optional, List

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from mdp.models.base import Base
from mdp.models.column import MetaColumn


class MetaTable(Base):
    __tablename__ = 'meta_table'

    id = Column(Integer, primary_key=True)
    database = Column(String(length=50))
    schema = Column(String(length=50))
    name = Column(String(length=50))
    description = Column(String(length=200))
    owner = Column(String(length=20))

    columns = relationship('meta_column')

    def __init__(
            self,
            database: str,
            schema: str,
            name: str,
            description: Optional[str] = None,
            owner: Optional[str] = None
    ):
        self.database = database
        self.schema = schema
        self.name = name
        self.description = description
        self.owner = owner

        self.columns: Optional[List[MetaColumn]] = None
