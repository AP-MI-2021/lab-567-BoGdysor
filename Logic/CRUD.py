from Domain.cheltuiala import creeaza_cheltuiala, get_id


def create(lst_cheltuieli, id_apartament : int, nr_apartament, suma, data, tip):
    """

    :param lst_cheltuieli:
    :param nr_apartament:
    :param suma:
    :param data:
    :param tip:
    :param id_apartament:
    :return:
    """
    cheltuiala = creeaza_cheltuiala(id_apartament, nr_apartament, suma, data, tip)
    # lst_cheltuieli.append(cheltuiala)
    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, id_cheltuiala: int = None):
    cheltuiala_cu_id = None
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_cu_id = cheltuiala
    if cheltuiala_cu_id:
        return cheltuiala_cu_id
    return lst_cheltuieli


def update(lst_cheltuieli, new_cheltuiela):
    new_cheltuieli = []
    for cheltuiela in lst_cheltuieli:
        if get_id(cheltuiela) != get_id(new_cheltuiela):
            new_cheltuieli.append(cheltuiela)
        else:
            new_cheltuieli.append(new_cheltuiela)
    return new_cheltuieli


def delete(lst_cheltuieli, id_cheltuiei):
    new_cheltuieli = []
    for cheltuieli in lst_cheltuieli:
        if get_id(cheltuieli) != id_cheltuiei:
            new_cheltuieli.append(cheltuieli)
    return new_cheltuieli
