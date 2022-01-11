from typing import Optional

from pydantic import BaseModel


class MetaTableBase(BaseModel):
    database: Optional[str] = None
    schema: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    owner: Optional[str] = None
    update_frequency: Optional[str] = None


class MetaTableCreate(MetaTableBase):
    database: str
    schema: str
    name: str


class MetaTableUpdate(MetaTableBase):
    pass


class MetaTableInDBBase(MetaTableBase):
    id: int
    database: str
    schema: str
    name: str

    class Config:
        orm_mode = True


class MetaTable(MetaTableInDBBase):
    pass


class MetaTableInDB(MetaTableInDBBase):
    pass
