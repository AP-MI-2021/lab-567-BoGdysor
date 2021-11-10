from Domain.cheltuiala import creeaza_cheltuiala
from Logic.stergere_apartament import stergere_nr_aprtament


def get_data():
    return [
        creeaza_cheltuiala(12, 69, 6969, "20-10-2021", "canal"),
        creeaza_cheltuiala(13, 191, 100, "21-10-2021", "alte cheltuieli"),
        creeaza_cheltuiala(14, 121, 1001, "11-11-2021", "intretinere")
    ]


def test_stergere_apartament():
    lst_cheltuieli = get_data()
    lst_cheltuieli = stergere_nr_aprtament(lst_cheltuieli, 69, [], [])
    assert lst_cheltuieli == [[13, 191, 100, '21-10-2021', 'alte cheltuieli'],
                              [14, 121, 1001, '11-11-2021', 'intretinere']]


test_stergere_apartament()
