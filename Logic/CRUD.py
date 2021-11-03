from Domain.cheltuiala import creeaza_cheltuiala, get_id


def create(lst_cheltuieli, id_cheltuiala: int, nr_apartament, suma, data, tip):
    """
    Creaza o cheltuiala
    :param lst_cheltuieli:lista cu cheltuielile deja existente
    :param id_cheltuiala: id-ul cheltuielii
    :param nr_apartament:numarul apartamentuilui
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tip: tip-ul cheltuielii
    :return: cheltuiala adaugata la lst_chetluieli
    """
    if tip!='canal' and tip!='intretinere' and tip!='alte cheltuieli':
        raise ValueError("Acest tip este invalid")
    if read(lst_cheltuieli, id_cheltuiala) is not None:
        raise ValueError("Deja exista o cheltuiala cu id-ul {0}".format(id_cheltuiala))
    cheltuiala = creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tip)

    # lst_cheltuieli.append(cheltuiala)
    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, id_cheltuiala: int = None):
    """
    Citeste o cheltuiala din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli existente
    :param id_cheltuiala: id-ul cheltuielii pe care o sa o citim
    :return:cheltuiala_cu_id daca aceasta exista in lista, lst_cheltuieli in caz contrar
    """
    cheltuiala_cu_id = None

    if not id_cheltuiala:
        return lst_cheltuieli
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_cu_id = cheltuiala
    if cheltuiala_cu_id:
        return cheltuiala_cu_id
    else:
        return None


def update(lst_cheltuieli, new_cheltuiela):
    """
    Updateaza o cheltuiala din lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli existente
    :param new_cheltuiela: cheltuiala pe care vrem sa o modficam
    :return:new_cheltuieli - noua lista cu cheltuieli dupa modificarea cheltuielii
    """
    new_cheltuieli = []

    if read(lst_cheltuieli, get_id(new_cheltuiela)) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul {0} pe care o sa o actualizam".format(get_id(new_cheltuiela)))

    for cheltuiela in lst_cheltuieli:
        if get_id(cheltuiela) != get_id(new_cheltuiela):
            new_cheltuieli.append(cheltuiela)
        else:
            new_cheltuieli.append(new_cheltuiela)
    return new_cheltuieli


def delete(lst_cheltuieli, id_cheltuiei):
    """
    Stergerea unei cheltuieli
    :param lst_cheltuieli: lista cu cheltuielile existente
    :param id_cheltuiei: cheltuiala pe care vrem sa o stergem
    :return: new_cheltuieli - boua lista cu cheltuieli dupa stergerea cheltuielii alese
    """
    if read(lst_cheltuieli, id_cheltuiei) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul {0} pe care o sa o stergem".format(id_cheltuiei))
    new_cheltuieli = []
    for cheltuieli in lst_cheltuieli:
        if get_id(cheltuieli) != id_cheltuiei:
            new_cheltuieli.append(cheltuieli)
    return new_cheltuieli
