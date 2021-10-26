def creeaza_cheltuiala(nr_apartament, suma, data, tip):
    """
    Creeaza cheltuiala
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
