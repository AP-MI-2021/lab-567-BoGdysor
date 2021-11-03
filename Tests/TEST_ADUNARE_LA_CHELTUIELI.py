from Domain.cheltuiala import get_suma, creeaza_cheltuiala
from Logic.adunare_cheltuieli import adunare_cheltuieli


def get_data():
    return [
        creeaza_cheltuiala(12, 69, 6969, "20/10/2021", "canal"),
        creeaza_cheltuiala(13, 191, 100, "21/10/2021", "alte cheltuieli"),
        creeaza_cheltuiala(14, 121, 1001, "10/20/2021", "intretinere")
    ]


def test_adunare_cheltuieli():
    data = "10/20/2021"
    cheltuieli = get_data()
    cheltuieli_new = []
    adunare_cheltuieli(cheltuieli_new, 100, data)
    assert get_suma(cheltuieli_new[2]) == get_suma(cheltuieli[2])
