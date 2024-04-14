from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Settings

settings = Settings()
db_host = settings.DB_HOST
db_port = settings.DB_PORT
db_name = settings.DB_NAME
db_user = settings.DB_USER
db_password = settings.DB_PASSWORD

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
Base = declarative_base()


class EngineConnection:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=500)

    def get_session(self):
        session_local = sessionmaker(autoflush=False, autocommit=False, bind=self.engine)
        return session_local()

    def get_connection(self):
        return self.engine.connect()


def get_db():
    engine_conn = EngineConnection()
    try:
        session = engine_conn.get_session()
        yield session
    finally:
        session.close()
