from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mdp.models.base import Base


class MetaCode(Base):
    __tablename__ = 'meta_code'

    id = Column(Integer, primary_key=True)
    column_id = Column(Integer, ForeignKey('meta_column.id'))
    name = Column(String(length=50))
    description = Column(String(length=100))

    column = relationship('MetaColumn', back_populates='codes')
