from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base

connection = {
    "host" : "XXXXX",
    "dbname" : "XXXXX",
    "user" : "XXXXX",
    "password" : "XXXXX",
}

def get_engine(host, dbname, user, password):
    url = f"postgresql://{user}:{password}@{host}/{dbname}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine

def engine_settings():
    keys = ['host','dbname','user','password']
    if not all(key in keys for key in connection.keys()):
        raise Exception('Bad config file')
    return get_engine(connection['host'],
                      connection['dbname'],
                      connection['user'],
                      connection['password'])

def sessions():
    engine = engine_settings()
    session = sessionmaker(bind=engine)
    return session

engine = engine_settings()
session = sessions()
base = declarative_base()