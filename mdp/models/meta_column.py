"""Meta column"""
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Index
from sqlalchemy.orm import relationship

from mdp.models.base import Base


class MetaColumn(Base):
    """Meta Column
    """
    __tablename__ = 'meta_column'

    id = Column(Integer, primary_key=True)
    meta_table_id = Column(Integer, ForeignKey('meta_table.id'))
    name = Column(String(length=50))
    data_type = Column(String(length=20))
    description = Column(String(length=100))
    is_pk = Column(Boolean, nullable=False)
    nullable = Column(Boolean, nullable=False)

    table = relationship('MetaTable', back_populates='columns')
    codes = relationship('MetaCode', back_populates='column')

    __table_args__ = (
        Index('idx_meta_column', meta_table_id, name, unique=True),
        {'extend_existing': True}
    )

    def __init__(self, name, data_type, description, is_pk, nullable):
        self.name = name
        self.data_type = data_type
        self.description = description
        self.is_pk = is_pk
        self.nullable = nullable
