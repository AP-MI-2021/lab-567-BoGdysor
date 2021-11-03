from Domain.cheltuiala import get_data, get_suma, creeaza_cheltuiala, get_id, get_nr_apartament, get_tip


def adunare_cheltuieli(lst_cheltuieli, valoare, data):
    result = []
    for cheltuiala in lst_cheltuieli:
        if get_data(cheltuiala) == data:
            suma_noua = get_suma(cheltuiala) + valoare
            result.append(
                creeaza_cheltuiala(get_id(cheltuiala), get_nr_apartament(cheltuiala), suma_noua, data,
                                   get_tip(cheltuiala))
            )
        else:
            result.append(cheltuiala)
    return result
