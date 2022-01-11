from typing import Optional

from pydantic import BaseModel


class MetaColumnBase(BaseModel):
    name: Optional[str] = None
    data_type: Optional[str] = None
    description: Optional[str] = None
    is_pk: bool = False
    nullable: bool = False


class MetaColumnCreate(MetaColumnBase):
    name: str
    data_type: str


class MetaColumnUpdate(MetaColumnBase):
    pass


class MetaColumnInDBBase(MetaColumnBase):
    id: int
    meta_table_id: int
    name: str

    class Config:
        orm_mode = True


class MetaColumn(MetaColumnInDBBase):
    pass


class MetaColumnInDB(MetaColumnInDBBase):
    pass
