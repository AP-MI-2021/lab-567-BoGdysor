from Domain.cheltuiala import creeaza_cheltuiala, get_suma
from Logic.adunare_cheltuieli import adunare_cheltuieli


def get_data():
    return [
        creeaza_cheltuiala(12, 69, 6969, "20-10-2021", "canal"),
        creeaza_cheltuiala(13, 191, 100, "21-10-2021", "alte cheltuieli"),
        creeaza_cheltuiala(14, 121, 1001, "11-10-2021", "intretinere")
    ]


def test_adunare_cheltuieli():
    data = "11-10-2021"
    cheltuieli = get_data()
    cheltuieli_new = []
    cheltuieli_new = adunare_cheltuieli(cheltuieli, 100, data, [], [])
    assert get_suma(cheltuieli_new[2]) == get_suma(cheltuieli[2])+100


test_adunare_cheltuieli()
