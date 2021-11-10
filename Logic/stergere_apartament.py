from Domain.cheltuiala import get_nr_apartament


def stergere_nr_aprtament(lst_cheltuieli, nr_aprtament, undo_list, redo_list):
    """
    Stergerea cheltuielilor de la nr apartament-ului dat
    :param lst_cheltuieli: lista cheltuililor
    :param nr_aprtament: nr apratamentului
    :param undo_list: lista de undo
    :param redo_list:lista de redo
    :return: lista cu cheltuiliile updatate
    """
    new_lst_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_aprtament:
            new_lst_cheltuieli.append(cheltuiala)
    if len(new_lst_cheltuieli) == len(lst_cheltuieli):
        raise ValueError('Nu exista o cheltuiala cu acest numar de apartament')
    undo_list.append(lst_cheltuieli)
    redo_list.clear()
    return new_lst_cheltuieli
