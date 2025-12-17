import sys

sys.path.append("/home/Hirmaan/projects/module-auth/")

from sqlmodel import SQLModel, create_engine


DB_NAME = "authdb"
DB_URL = "localhost:5432"


def createEngine():
    try:
        engine = create_engine(
            DB_URL, echo=True
        )  # what is the echo mode ? : to better understand whta happned in the background
        print("engine created")
        return engine
    except Exception as e:
        print(f"create engine error : {e}")


def CreateDBAndTables(engine):
    try:
        SQLModel.metadata.create_all(
            engine
        )  # when you use Table attrebiute in the table class you should to migrate metadata
    except Exception as e:
        print(f"CreateDBAndTables has error : {e}")
