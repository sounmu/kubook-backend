import os
import paramiko
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Settings

settings = Settings()

ssh_host = settings.SSH_HOST
ssh_port = settings.SSH_PORT
ssh_username = settings.SSH_USERNAME
ssh_key_filename = settings.SSH_KEYFILE  # Update this with the correct path to your key file

if os.access(ssh_key_filename, os.R_OK):
    print(f"You have permission to read the key file: {ssh_key_filename}")
else:
    print(f"You do not have permission to read the key file: {ssh_key_filename}")
    exit(1)  # Exit the program if you don't have permission to read the key file

db_host = settings.DB_HOST
db_port = settings.DB_PORT
db_name = settings.DB_NAME
db_user = settings.DB_USER
db_password = settings.DB_PASSWORD

print(f"Connecting to SSH host: {ssh_host}:{ssh_port} with username: {ssh_username}")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

local_port = 3307  # Local port to forward to remote MySQL server
ssh_tunnel = None

try:
    ssh_client.connect(hostname=ssh_host, port=ssh_port, username=ssh_username, key_filename=ssh_key_filename,
                       timeout=30)
    print("SSH connection successful.")
    # remote_bind_address = (db_host, db_port)
    # local_bind_address = ('localhost', local_port)
    #
    # try:
    #     ssh_tunnel = ssh_client.get_transport().open_channel('direct-tcpip', remote_bind_address, local_bind_address)
    #     print("SSH tunnel successfully established.")
    # except Exception as e:
    #     print(f"Error creating SSH tunnel: {e}")

except Exception as e:
    print(f"Error connecting to SSH: {e}")
    exit(1)  # Exit the program if SSH connection fails

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

def get_db_session():
    engine_conn = EngineConnection()
    session = engine_conn.get_session()
    try:
        yield session
        print('get db session')
    finally:
        session.close()

# Close the SSH tunnel and client
if ssh_tunnel:
    ssh_tunnel.close()
if ssh_client:
    ssh_client.close()

get_db_session()
