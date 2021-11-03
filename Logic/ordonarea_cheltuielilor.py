from Domain.cheltuiala import get_suma


def suma(cheltuieli):
    return get_suma(cheltuieli)


def ord_chelt_dupa_suma_desc(lst_cheltuieli):
    new_list = sorted(lst_cheltuieli, key=suma, reverse=True)
    return new_list
