from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from constants import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_DB,
    POSTGRES_PORT
)

engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

Session = sessionmaker(bind=engine)
session = Session()
