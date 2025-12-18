import sys

sys.path.append("/home/Hirmaan/projects/module-auth/")

from models.db import createEngine, CreateDBAndTables
from sqlmodel import Session
from utils.loger import ConsoleLogger

logger = ConsoleLogger()


class Repository:
    """this is the repository desgin pattern"""

    def __init__(self) -> None:
        self.engine = createEngine()
        CreateDBAndTables(self.engine)

    def insert(self, row):
        try:
            with Session(self.engine) as session:
                session.add(row)

                session.commit()
            logger.success("insert successfully")
            return True
        except Exception as e:
            logger.error("insert has error", e)
            return False

    def edit(self, row):
        pass

    def update(self, row):
        pass

    def delete(self, row):
        pass
