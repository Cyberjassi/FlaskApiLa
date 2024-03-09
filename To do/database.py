from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#make a variable for database location-
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
#engine db in arugument not many thread avaible
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()