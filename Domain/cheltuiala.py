def creeaza_cheltuiala(id_cheltuiala: int, nr_apartament, suma, data, tip):
    """
    Creeaza o  cheltuiala
    :param id_cheltuiala: id-ul apartamentului
    :param nr_apartament: nr_apartament-ului,
    :param suma: suma cheltuielii
    :param data: data cheltuielii
    :param tip: tipul cheltuielii : intretinere/canal/alte cheltuieli

    :return: o cheltuiala
    """
    return {
        'nr_apartament': nr_apartament,
        'suma': suma,
        'data': data,
        'tip': tip,
        'id_cheltuiala': id_cheltuiala,
    }


def get_nr_apartament(cheltuiala):
    """
    Getter penrtu numarul apartamentului
    :param cheltuiala: O cheltuiala
    :return: Nr de apartament al Cheltuielii
    """
    return cheltuiala['nr_apartament']


def get_suma(cheltuiala):
    """
    Getter pentru suma cheltuielii
    :param cheltuiala: o cheltuiala
    :return: suma cheltuielii
    """
    return cheltuiala['suma']


def get_data(cheltuiala):
    """
    Getter pentru data cheltuielii
    :param cheltuiala: O cheltuiala
    :return:suma cheltuielii
    """
    return cheltuiala['data']


def get_tip(cheltuiala):
    """
    Getter pentru tip-ul cheltuielii
    :param cheltuiala: O cheltuiala
    :return:Tip-ul cheltuielii
    """
    return cheltuiala['tip']


def get_id(cheltuiala):
    """
    Getter pentru id-ul cheltuielii
    :param cheltuiala: O cheltuiala
    :return:Id-ul cheltuielii
    """
    return cheltuiala['id_cheltuiala']


def get_str(cheltuiala):
    """
    Getter pentru mesajul cu detaliile cheltuielii
    :param cheltuiala: O cheltuiala
    :return:Mesajul cu detaliile cheltuielii
    """
    return "Cheltuiala cu id-ul {0},cu numarul de apartament {1},are de platit suma {2},in data de {3}, avand tipul {4}".format(
        get_id(cheltuiala), get_nr_apartament(cheltuiala), get_suma(cheltuiala), get_data(cheltuiala),
        get_tip(cheltuiala))
