import sys

sys.path.append("/home/Hirmaan/projects/module-auth/")

from models.db import createEngine, CreateDBAndTables
from sqlmodel import Session, select
from utils.loger import ConsoleLogger

logger = ConsoleLogger()


class Repository:
    """this is the repository desgin pattern"""

    def __init__(self) -> None:
        self.engine = createEngine()
        CreateDBAndTables(self.engine)

    def selectAll(self, table):
        try:
            with Session(self.engine) as session:
                statement = select(table)
                results = list(session.exec(statement))
                session.expunge_all()

            logger.success("selectAll successfully")
            return results
        except Exception as e:
            logger.error("selectAll has error", e)

    def selectWhere(self, table, condition):
        try:
            with Session(self.engine) as session:
                statement = select(table).where(condition)
                results = list(session.exec(statement))
                session.expunge_all()

            logger.success("selectAll successfully")
            return results
        except Exception as e:
            logger.error("selectAll has error", e)

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
