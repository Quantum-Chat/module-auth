from models.repository import Repository
from models.models import Client


def main():
    repo = Repository()
    newRow = Client(id=1,token="updated")
    result = repo.update(Client,1,newRow)

    print(result)


if __name__ == "__main__":
    main()