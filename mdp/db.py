from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mdp.config import settings

engine = create_engine(settings.SQLALCHEMY_URI)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
