from typing import Optional

from pydantic import BaseModel


class TableBase(BaseModel):
    database: Optional[str] = None
    schema: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    owner: Optional[str] = None
    update_frequency: Optional[str] = None


class TableCreate(TableBase):
    database: str
    schema: str
    name: str


class TableUpdate(TableBase):
    pass


class TableInDBBase(TableBase):
    id: str
    database: str
    schema: str
    name: str

    class Config:
        orm_mode = True


class Table(TableInDBBase):
    pass


class TableInDB(TableInDBBase):
    pass
