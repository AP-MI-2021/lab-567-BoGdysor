from Logic.CRUD import create
from Tests.TEST_CRUD import test_crud
from UserInterface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = create(cheltuieli, 12, 888, 1001, '10/08/2021', "canal")
    run_ui(cheltuieli)


if __name__ == '__main__':
    test_crud()
    main()
