import sys

# sys.path.append("F:/Projects/Quantum/back-end/Microservice/auth")
# sys.path.append("/home/Hirmaan/projects/module-auth/") # for linux

from sqlmodel import SQLModel, create_engine
from utils.loger import ConsoleLogger


DB_NAME = "clients"
DB_URL = "postgresql://postgres:postgres@localhost:5433/clients" # port changed in docker

logger = ConsoleLogger()


def createEngine():
    try:
        engine = create_engine(
            DB_URL, echo=True
        )  # what is the echo mode ? : to better understand whta happned in the background
        logger.success("engine created successfully")
        return engine
    except Exception as e:
        logger.error("create engine error", e)


def CreateDBAndTables(engine):
    try:
        SQLModel.metadata.create_all(
            engine
        )  # when you use Table attrebiute in the table class you should to migrate metadata
        logger.success("config db successfully")
    except Exception as e:
        logger.error("config db has error", e)
