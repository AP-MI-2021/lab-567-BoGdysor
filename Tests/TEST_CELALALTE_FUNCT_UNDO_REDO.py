from Logic.CRUD import create
from Logic.Undo_Redo import do_undo, do_redo
from Logic.adunare_cheltuieli import adunare_cheltuieli
from Logic.stergere_apartament import stergere_nr_aprtament


def test_stergere_do_redo():
    undo_list = []
    redo_list = []
    lst_cheltuieli = []
    lst_cheltuieli = create(lst_cheltuieli, 99, 124, 123, '11-10-2021', 'canal', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 101, 126, 220, '12-10-2021', 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 103, 128, 420, '13-10-2021', 'intretinere', undo_list, redo_list)
    before_undo = lst_cheltuieli
    lst_cheltuieli = stergere_nr_aprtament(lst_cheltuieli, 124, undo_list, redo_list)
    assert lst_cheltuieli == [[101, 126, 220, '12-10-2021', 'alte cheltuieli'],
                              [103, 128, 420, '13-10-2021', 'intretinere']]
    lst_cheltuieli = do_undo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 3
    lst_cheltuieli = do_redo(undo_list, redo_list, lst_cheltuieli)
    assert len(lst_cheltuieli) == 2


def test_suma_valoare_luni():
    undo_list = []
    redo_list = []
    lst_cheltuieli = []
    lst_cheltuieli = create(lst_cheltuieli, 99, 124, 123, '11-10-2021', 'canal', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 101, 126, 220, '12-10-2021', 'alte cheltuieli', undo_list, redo_list)
    lst_cheltuieli = create(lst_cheltuieli, 103, 128, 420, '13-10-2021', 'intretinere', undo_list, redo_list)

    lst_cheltuieli = adunare_cheltuieli(lst_cheltuieli, 1020, '11-10-2021', undo_list, redo_list)
    assert lst_cheltuieli == [[99, 124, 1143.0, '11-10-2021', 'canal'], [101, 126, 220, '12-10-2021', 'alte cheltuieli'],
                              [103, 128, 420, '13-10-2021', 'intretinere']]
    lst_cheltuieli = do_undo(undo_list,redo_list,lst_cheltuieli)
    assert  lst_cheltuieli == [[99, 124, 123, '11-10-2021', 'canal'], [101, 126, 220, '12-10-2021', 'alte cheltuieli'],
                               [103, 128, 420, '13-10-2021', 'intretinere']]
    lst_cheltuieli = do_redo(undo_list,redo_list,lst_cheltuieli)
    assert  lst_cheltuieli == [[99, 124, 1143.0, '11-10-2021', 'canal'], [101, 126, 220, '12-10-2021', 'alte cheltuieli'],
                              [103, 128, 420, '13-10-2021', 'intretinere']]

