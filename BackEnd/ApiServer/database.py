import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import PostgresDsn

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'whesoyam1W'
print(os.environ.values())
if os.environ.get('POSTGRES_SERVER'):
    POSTGRES_SERVER = os.environ.get('POSTGRES_SERVER')
else:
    POSTGRES_SERVER = '127.0.0.1'
POSTGRES_DB = 'leader_hack'

SQLALCHEMY_DATABASE_URL = PostgresDsn.build(
    scheme="postgresql",
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_SERVER,
    path=f"/{POSTGRES_DB or ''}",
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
