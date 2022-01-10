from mdp import crud, schemas
from mdp.core.config import settings
from mdp.db import provide_session


@provide_session
def init_db(session=None):
    user = crud.user.get_by_username(username=settings.FIRST_SUPERUSER, db=session)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True
        )
        user = crud.user.create(db=session, obj_in=user_in)
    return user


if __name__ == '__main__':
    init_db()
