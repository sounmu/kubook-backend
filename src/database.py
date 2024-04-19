from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings

settings = Settings()

ssh_host = settings.SSH_HOST
ssh_port = settings.SSH_PORT
ssh_username = settings.SSH_USERNAME
ssh_key_filename = settings.SSH_KEYFILE

db_host = settings.DB_HOST
db_port = settings.DB_PORT
db_name = settings.DB_NAME
db_user = settings.DB_USER
db_password = settings.DB_PASSWORD

local_host = 'localhost'
local_port = 3307 

Base = declarative_base()

class SSHConnection:
    def __init__(self):
        self.ssh_host = ssh_host
        self.ssh_port = ssh_port
        self.ssh_username = ssh_username
        self.ssh_key_filename = ssh_key_filename
        self.remote_bind_address = (db_host, db_port)
        self.local_bind_address = (local_host, local_port)
        self.ssh_client = None

    def check_ssh_key_permission(self):
        try:
            with open(self.ssh_key_filename, 'r'):
                print(f"You have permission to read the key file: {self.ssh_key_filename}")
        except PermissionError:
            print(f"You do not have permission to read the key file: {self.ssh_key_filename}")
            exit(1)

    def connect(self):
        print(f"Connecting to SSH host: {self.ssh_host}:{self.ssh_port} with username: {self.ssh_username}")
        try:
            self.check_ssh_key_permission()
            self.ssh_client = SSHTunnelForwarder(
                self.ssh_host,
                self.ssh_port,
                ssh_username=self.ssh_username,
                ssh_pkey=self.ssh_key_filename,
                remote_bind_address=self.remote_bind_address,
                local_bind_address=self.local_bind_address,
            )
        except Exception as e:
            print(f"Error connecting to SSH: {e}")
            exit(1)
        else :
            print("SSH connection successful.")
            self.ssh_client.start()

    def close(self):
        # Close the SSH tunnel and client
        if self.ssh_client:
            self.ssh_client.stop()

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

ssh_connection = SSHConnection()
ssh_connection.connect() 

def get_db_session():
    engine_conn = EngineConnection()
    session = engine_conn.get_session()
    return session

# Fetch data from the server database
with get_db_session() as session:
    print("Server Data:")
    server_data = session.execute(text("select * from service_setting;")).fetchall()
    if server_data :
        for row in server_data:
            print(row)
    else : print('No data')