from Logic.CRUD import create
from Logic.Undo_Redo import do_undo, do_redo


def test_undo_redo_lab_7():
    start_program = []
    undo_list = []
    redo_list = []

    start_program = create(start_program, 99, 124, 123, '11-10-2021', 'canal', undo_list, redo_list)
    start_program = create(start_program, 101, 126, 220, '12-10-2021', 'alte cheltuieli', undo_list, redo_list)
    start_program = create(start_program, 103, 128, 420, '13-10-2021', 'intretinere', undo_list, redo_list)
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 0
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 0
    start_program = create(start_program, 99, 124, 123, '11-10-2021', 'canal', undo_list, redo_list)
    start_program = create(start_program, 101, 126, 220, '12-10-2021', 'alte cheltuieli', undo_list, redo_list)
    start_program = create(start_program, 103, 128, 420, '13-10-2021', 'intretinere', undo_list, redo_list)

    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 3
    start_program = do_undo(undo_list, redo_list, start_program)
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 3
    start_program = do_undo(undo_list, redo_list, start_program)
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = create(start_program, 110, 128, 420, '14-10-2021', 'intretinere', undo_list, redo_list)
    assert len(start_program) == 2
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 1
    start_program = do_undo(undo_list, redo_list, start_program)
    assert len(start_program) == 0
    start_program = do_redo(undo_list, redo_list, start_program)
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 2
    start_program = do_redo(undo_list, redo_list, start_program)
    assert len(start_program) == 2


test_undo_redo_lab_7()
