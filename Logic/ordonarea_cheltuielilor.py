from Domain.cheltuiala import get_suma


def suma(cheltuieli):
    return get_suma(cheltuieli)


def ord_chelt_dupa_suma_desc(lst_cheltuieli, ):
    """
    Ordoneaza lista de cheltuieli dupa suma, descrescator
    :param lst_cheltuieli:  lista de cheltuieli
    :return: o noua lista cu cheltuieliile orodnate descrescator dupa suma
    """
    new_list = sorted(lst_cheltuieli, key=suma, reverse=True)
    return new_list
