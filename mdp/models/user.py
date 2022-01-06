from sqlalchemy import Column, String, Integer, Boolean

from mdp.models.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True, unique=True, nullable=False)
    first_name = Column(String(20))
    last_name = Column(String(20))
    email = Column(String(100), index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
