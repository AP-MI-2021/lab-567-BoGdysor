from Domain.cheltuiala import creeaza_cheltuiala
from Logic.CRUD import create
from Logic.Undo_Redo import do_undo, do_redo


def get_data():
    return [
        creeaza_cheltuiala(12, 69, 6969, "20-10-2021", "canal"),
        creeaza_cheltuiala(13, 191, 100, "21-10-2021", "alte cheltuieli"),
        creeaza_cheltuiala(14, 121, 1001, "23-10-2021", "intretinere")
    ]


def test_undo_redo():
    lst_cheltuieli = get_data()
    undo_list = []
    redo_list = []
    params = (1234, 101, 799, '12-01-2021', 'intretinere')
    new_lst_cheltuieli = create(lst_cheltuieli, *params, undo_list,
                                redo_list)
    new_lst_cheltuieli = do_undo(undo_list, redo_list, new_lst_cheltuieli)
    assert new_lst_cheltuieli == lst_cheltuieli
    new_lst_cheltuieli = do_undo(undo_list, redo_list, new_lst_cheltuieli)  # undo_list = None => nu se intampla nimic
    assert new_lst_cheltuieli == lst_cheltuieli
    new_lst_cheltuieli = do_redo(undo_list, redo_list, new_lst_cheltuieli)
    assert len(new_lst_cheltuieli) == len(lst_cheltuieli) + 1
    new_lst_cheltuieli = do_undo(undo_list, redo_list, new_lst_cheltuieli)

test_undo_redo()