import sys

sys.path.append("/home/Hirmaan/projects/module-auth/")


from models.repository import Repository
from models.models import Client


def main():
    repo = Repository()
    result = repo.selectAll(Client)

    if not result:
        result = []

    for item in iter(result):
        print(item)


if __name__ == "__main__":
    main()
