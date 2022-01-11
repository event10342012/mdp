from mdp.crud.base import CRUDBase
from mdp.models.meta_table import MetaTable
from mdp.schemas.meta_table import MetaTableCreate, MetaTableUpdate


class CRUDMetaTable(CRUDBase[MetaTable, MetaTableCreate, MetaTableUpdate]):
    pass


meta_table = CRUDMetaTable(MetaTable)
