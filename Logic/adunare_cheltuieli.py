from datetime import datetime

from Domain.cheltuiala import get_data, get_suma, creeaza_cheltuiala, get_id, get_nr_apartament, get_tip
from Logic.CRUD import create


def adunare_cheltuieli(lst_cheltuieli, valoare, data, undo_list: list, redo_list: list):
    """
    Adunam valoarea la o suma dintr-o data anume
    :param lst_cheltuieli:lista de cheltuili
    :param valoare:valoarea pe care o sa o adaugam la suma
    :param data: data la care adaugam
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return: result - lista cu cheltuieli updata
    """
    result = []
    ok = 0
    format = "%d-%m-%Y"
    if datetime.strptime(data, format) is None:
        raise ValueError("Nu este bun formatul datii")
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            suma_noua = get_suma(cheltuiala) + valoare
            result.append(
                creeaza_cheltuiala(get_id(cheltuiala), get_nr_apartament(cheltuiala),float(suma_noua),
                                   get_data(cheltuiala),
                                   get_tip(cheltuiala))
            )
            ok = ok+1
        else:
            result.append(cheltuiala)
    if ok == 0:
        raise ValueError("Nu s-a gasit o cheltuiala din data {0}".format(data))
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return result
