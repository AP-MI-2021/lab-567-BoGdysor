from Domain.cheltuiala import creeaza_cheltuiala
from Logic.suma_lunara import suma_lunara


def get_data():
    return [
        creeaza_cheltuiala(12, 69, 6969, "20-10-2021", "canal"),
        creeaza_cheltuiala(13, 191, 100, "21-11-2021", "alte cheltuieli"),
        creeaza_cheltuiala(14, 121, 1001, "23-8-2021", "intretinere")
    ]


def test_suma_luni():
    cheltuieli = get_data()
    assert suma_lunara(cheltuieli) == {'10': [6969], '11': [100], '8': [1001]}
    cheltuieli.append(creeaza_cheltuiala(14, 121, 1011, "23-7-2021", "intretinere"))
    assert suma_lunara(cheltuieli) == {'10': [6969], '11': [100], '8': [1001], '7': [1011]}