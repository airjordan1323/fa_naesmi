import ormar
import sqlalchemy
import databases
ORMAR_DATABASE_URL = "postgresql://admin:admin@localhost/fa_naesmi"

metadata = sqlalchemy.MetaData()
database = databases.Database(ORMAR_DATABASE_URL)
engine = sqlalchemy.create_engine(ORMAR_DATABASE_URL)


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
