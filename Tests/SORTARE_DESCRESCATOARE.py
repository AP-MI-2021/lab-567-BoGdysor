from Domain.cheltuiala import creeaza_cheltuiala, get_suma
from Logic.ordonarea_cheltuielilor import ord_chelt_dupa_suma_desc


def get_data():
    return [
        creeaza_cheltuiala(12, 69, 6969, "20-10-2021", "canal"),
        creeaza_cheltuiala(13, 191, 100, "21-10-2021", "alte cheltuieli"),
        creeaza_cheltuiala(14, 121, 1001, "23-10-2021", "intretinere")
    ]


def test_ord_chelt_dupa_suma_desc():
    lst = get_data()
    ord_lst = ord_chelt_dupa_suma_desc(lst)

    assert get_suma(ord_lst[2]) > get_suma(ord_lst[1]) > get_suma(ord_lst[0])


test_ord_chelt_dupa_suma_desc()
