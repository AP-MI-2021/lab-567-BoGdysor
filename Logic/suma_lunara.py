from Domain.cheltuiala import get_data, get_suma


def suma_lunara(lst_cheltuieli):
    """
    Creeam un dictionar avand ca si key luna si valoarea este o lista ce contine sumele din luna respectiva
    :param lst_cheltuieli: lista de cheltuieli
    :return: months - dictionar avand ca si key luna si valoarea este o lista ce contine sumele din luna respectiva
    """
    months = dict()
    for cheltuiala in lst_cheltuieli:
        date = get_data(cheltuiala)
        month = date.split('-')[1]
        if month not in months:
            months[month] = []
            months[month].append(get_suma(cheltuiala))
        else:
            months[month].append(get_suma(cheltuiala))
    return months
