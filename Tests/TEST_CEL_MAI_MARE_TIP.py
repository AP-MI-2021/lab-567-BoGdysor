from Domain.cheltuiala import creeaza_cheltuiala
from Logic.Cel_mai_mare_tip import cea_mai_mare_cheltuiala_tip


def get_data():
    return [
        creeaza_cheltuiala(12, 69, 6969, "20/10/2021", "canal"),
        creeaza_cheltuiala(13, 191, 100, "21/10/2021", "alte cheltuieli"),
        creeaza_cheltuiala(14, 121, 1001, "23/10/2021", "intretinere")
    ]


def test_cea_mai_mare_cheltuiala_tip():
    lst = get_data()
    assert cea_mai_mare_cheltuiala_tip(lst, "canal") == 6969
    assert cea_mai_mare_cheltuiala_tip(lst, "alte cheltuieli") == 100
    assert cea_mai_mare_cheltuiala_tip(lst, "intretinere") == 1001
