from sqlmodel import SQLModel, create_engine


DB_NAME = "lcoaldb"
DB_URL = "localhost:5432"


def createEngine():
    engine = create_engine(
        DB_URL, echo=True
    )  # what is the echo mode ? : to better understand whta happned in the background

    return engine


def CreateDBAndTables(engine):
    SQLModel.metadata.create_all(
        engine
    )  # when you use Table attrebiute in the table class you should to migrate metadata
