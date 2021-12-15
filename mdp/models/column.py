from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Index

from mdp.models.base import Base


class MetaColumn(Base):
    __tablename__ = 'meta_column'

    id = Column(Integer, primary_key=True)
    table_id = Column(Integer, ForeignKey('meta_table.id'))
    name = Column(String(length=50))
    data_type = Column(String(length=20))
    description = Column(String(length=50))
    is_pk = Column(Boolean, nullable=False)
    nullable = Column(Boolean, nullable=False)

    __table_args__ = (
        Index('idx_meta_column', table_id, name)
    )
