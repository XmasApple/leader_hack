from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = '1111'
POSTGRES_SERVER = '127.0.0.1'
POSTGRES_DB = 'leader_hack'

# SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@postgresserver/db'
# SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}'

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