from mdp.crud.base import CRUDBase
from mdp.models.meta_column import MetaColumn
from mdp.schemas.meta_column import MetaColumnCreate, MetaColumnUpdate


class CRUDMetaColumn(CRUDBase[MetaColumn, MetaColumnCreate, MetaColumnUpdate]):
    pass


meta_column = CRUDMetaColumn(MetaColumn)
