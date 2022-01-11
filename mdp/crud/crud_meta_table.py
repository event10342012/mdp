from mdp.crud.base import CRUDBase
from mdp.models.meta_table import MetaTable
from mdp.schemas.meta_table import TableCreate, TableUpdate


class CRUDMetaTable(CRUDBase[MetaTable, TableCreate, TableUpdate]):
    pass


meta_table = CRUDMetaTable(MetaTable)
