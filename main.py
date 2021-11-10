from Logic.CRUD import create
from Tests.FULL_TESTS import full_tests
from UserInterface.command_line import command_line
from UserInterface.console import run_ui


def main():
    cheltuieli = []
    undo_list = []
    redo_list = []
    cheltuieli = create(cheltuieli, 12, 888, 1001, '10-08-2021', "canal", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 13, 707, 100, "11-09-2021", "alte cheltuieli", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 14, 100, 6969, "12-10-2021", "intretinere", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 15, 90, 420, "13-09-2021", "canal", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 16, 70, 220, "14-09-2021", "alte cheltuieli", undo_list, redo_list)
    cheltuieli = create(cheltuieli, 17, 80, 250, "15-09-2021", "intretinere", undo_list, redo_list)
    command_line(cheltuieli)


if __name__ == '__main__':
    full_tests()
    main()
