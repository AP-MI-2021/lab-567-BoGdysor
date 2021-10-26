from Domain.cheltuiala import creeaza_cheltuiala, get_id
from Logic.CRUD import create, read, delete


def get_data():
    return [
        creeaza_cheltuiala(12, 69, 6969, "20/10/2021", "canal"),
        creeaza_cheltuiala(13, 191, 100, "21/10/2021", "alte cheltuieli"),
        creeaza_cheltuiala(14, 121, 1001, "23/10/2021", "intretinere")
    ]


def test_create():
    cheltuieli = get_data()
    params = (16, 991, 1001, "24/10/2021", "intretinere")
    new_c = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli, *params)
    assert new_c in new_cheltuieli
    assert len(new_cheltuieli) == len(cheltuieli) + 1


def test_read():
    cheltuieli = get_data()
    params = (15, 991, 1001, "24/10/2021", "intretinere")
    cheltuiala_noua = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli, *params)
    assert len(new_cheltuieli) == len(cheltuieli) + 1
    assert cheltuiala_noua in new_cheltuieli


def test_update():
    cheltuieli = get_data()
    chelt_1 = cheltuieli[1]
    assert read(cheltuieli, get_id(chelt_1)) == chelt_1
    assert read(cheltuieli, None) == cheltuieli


def test_delete():
    cheltuieli = get_data()
    to_delete = 12
    c_deleted = read(cheltuieli, to_delete)
    deleted = delete(cheltuieli, to_delete)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()

test_crud()