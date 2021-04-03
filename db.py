import sqlalchemy
import databases
from sqlalchemy.ext.declarative import declarative_base

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite.db")