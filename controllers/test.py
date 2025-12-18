import sys

sys.path.append("/home/Hirmaan/projects/module-auth/")


from models.repository import Repository
from models.models import Client


def main():
    row = Client(token="this a test for insert")
    repo = Repository()
    repo.insert(row)


if __name__ == "__main__":
    main()
