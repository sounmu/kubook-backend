from config import Settings
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

settings = Settings()


class EngineConnection:

    def __init__(self):
        if settings.ENVIRONMENT == "development":
            SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}@localhost:3307/{settings.DB_NAME}"
        elif settings.ENVIRONMENT == "production":
            SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        elif settings.ENVIRONMENT == "development-mj":
            SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.MJ_DB_USER}:{settings.MJ_DB_PASSWORD}@{settings.MJ_DB_HOST}:{settings.MJ_DB_PORT}/{settings.MJ_DB_NAME}"
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=500, connect_args={"connect_timeout": 100})
        self.session_local = sessionmaker(autoflush=False, autocommit=False, bind=self.engine)

    def get_session(self):
        return self.session_local()

    def get_connection(self):
        return self.engine.connect()


engine_conn = EngineConnection()


def get_db_session():
    session = engine_conn.get_session()
    return session
