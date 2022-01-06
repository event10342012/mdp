from fastapi import FastAPI

from mdp.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description='Meta data platform'
)
