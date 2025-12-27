from models.db import createEngine, CreateDBAndTables
from models.models import Client
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

    def update(self, table, rowId, newRow):
        try:
            with Session(self.engine) as session:
                statement = select(table).where(table.id == rowId)
                results = session.exec(statement)
                item = results.one()

                for field, value in newRow.__dict__.items():
                    if not field.startswith('_') and hasattr(item, field):
                        setattr(item, field, value)

                session.add(item)
                session.commit()
                session.refresh(item)

            logger.success("update successfully")
            return item
        except Exception as e:
            logger.error("update has error", e)
            return None

    def delete(self, table, rowId):
        try:
            with Session(self.engine) as session:
                statement = select(table).where(table.id == rowId)
                results = session.exec(statement)
                item = results.one()

                session.delete(item)
                session.commit()

            logger.success("delete successfully")
            return True
        except Exception as e:
            logger.error("delete has error", e)
            return False
