def creeaza_cheltuiala(id_apartament: int, nr_apartament, suma, data, tip):
    """
    Creeaza cheltuiala
    :param id_apartament: id-ul apartamentului
    :param nr_apartament: nr_apartament-ului,
    :param suma: suma cheltuielii
    :param data: data
    :param tip: tipul cheltuielii : intretinere/canal/alte cheltuieli

    :return: o cheltuiala
    """
    return {
        'nr_apartament': nr_apartament,
        'suma': suma,
        'data': data,
        'tip': tip,
        'id_apartament': id_apartament,
    }


def get_nr_apartament(cheltuiala):
    """
    Getter penrtu numarul apartamentului
    :param cheltuiala: Cheltuiala
    :return: Nr de apartament al Cheltuielii
    """
    return cheltuiala['nr_apartament']


def get_suma(cheltuiala):
    """

    :param cheltuiala:
    :return:
    """
    return cheltuiala['suma']


def get_data(cheltuiala):
    """

    :param cheltuiala:
    :return:
    """
    return cheltuiala['data']


def get_tip(cheltuiala):
    """

    :param cheltuiala:
    :return:
    """
    return cheltuiala['tip']


def get_id(cheltuiala):
    """

    :param cheltuiala:
    :return:
    """
    return cheltuiala['id_apartament']


def get_str(cheltuiala):
    return "Apartamentul cu id-ul {0},cu numarul de apartament {1},are de platit suma {2},la data de {3}, avand tipul {4}".format(
        get_id(cheltuiala), get_nr_apartament(cheltuiala), get_suma(cheltuiala), get_data(cheltuiala),
        get_tip(cheltuiala))
