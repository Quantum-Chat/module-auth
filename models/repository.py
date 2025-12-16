from db import createEngine, CreateDBAndTables
from sqlmodel import Session


class repository:
    """this is the repository desgin pattern"""

    def __init__(self) -> None:
        self.engine = createEngine()
        CreateDBAndTables(self.engine)

    def insert(self, row):
        try:
            with Session(self.engine) as session:
                session.add(row)

                session.commit()
            print("insert successfull")
            return True
        except:
            print("insert has problem")
            return False

    def edit(self, row):
        pass

    def update(self, row):
        pass

    def delete(self, row):
        pass
