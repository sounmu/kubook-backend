from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings
from ssh import SSHConnection

settings = Settings()

db_name = settings.DB_NAME
db_user = settings.DB_USER
db_password = settings.DB_PASSWORD

local_host = 'localhost'
local_port = 3307 

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{local_host}:{local_port}/{db_name}"

class EngineConnection:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=500, connect_args={"connect_timeout": 100})

    def get_session(self):
        session_local = sessionmaker(autoflush=False, autocommit=False, bind=self.engine)
        return session_local()

    def get_connection(self):
        return self.engine.connect()
    
    def close_engine(self):
        return self.engine.dispose()
    

def get_db_session():
    engine_conn = EngineConnection()
    session = engine_conn.get_session()
    return session

# Test to fetch data from the server database
ssh_connection = SSHConnection()
ssh_connection.connect() 

with get_db_session() as session:
    print("Server Data:")
    server_data = session.execute(text("select * from service_setting;")).fetchall()
    if server_data :
        for row in server_data:
            print(row)
    else : print('No data')
