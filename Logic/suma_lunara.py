from Domain.cheltuiala import get_data, get_suma


def suma_lunara(lst_cheltuieli):
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