import contextlib
from functools import wraps
from inspect import signature
from typing import Iterator, TypeVar, Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from mdp.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


@contextlib.contextmanager
def create_session() -> Iterator[Session]:
    """Contextmanager that will create and teardown a session."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


RT = TypeVar("RT")


def find_session_idx(func: Callable[..., RT]) -> int:
    """Find session index in function call parameter."""
    func_params = signature(func).parameters
    try:
        # func_params is an ordered dict -- this is the "recommended" way of getting the position
        session_args_idx = tuple(func_params).index("session")
    except ValueError:
        raise ValueError(f"Function {func.__qualname__} has no `session` argument") from None

    return session_args_idx


def provide_session(func: Callable[..., RT]) -> Callable[..., RT]:
    """
    Function decorator that provides a session if it isn't provided.
    If you want to reuse a session or run the function as part of a
    database transaction, you pass it to the function, if not this wrapper
    will create one and close it for you.
    """
    session_args_idx = find_session_idx(func)

    @wraps(func)
    def wrapper(*args, **kwargs) -> RT:
        if "session" in kwargs or session_args_idx < len(args):
            return func(*args, **kwargs)
        else:
            with create_session() as session:
                return func(*args, session=session, **kwargs)

    return wrapper
