from Domain.cheltuiala import get_suma, get_tip


def cea_mai_mare_cheltuiala_tip(lst_cheltuieli,  chelt_tip):
    """
    Determina cea mai mare suma dintr-un anumit tip
    :param lst_cheltuieli:  lista de cheltuieli
    :param chelt_tip: tipul cheltuielii la care vrem sa ii gasim cea mai mare cheltuiala tip
    :return: cea mai mare cheltuiala pentru tip-ul dat, None in caz ca nu exista acel tip
    """
    tip = {
        "intretinere": 0,
        "canal": 0,
        "alte cheltuieli": 0
    }
    for cheltuiala in lst_cheltuieli:
        if get_tip(cheltuiala) == "intretinere":
            if get_suma(cheltuiala) > tip["intretinere"]:
                tip["intretinere"] = get_suma(cheltuiala)
        elif get_tip(cheltuiala) == "canal":
            if get_suma(cheltuiala) > tip["canal"]:
                tip["canal"] = get_suma(cheltuiala)
        elif get_tip(cheltuiala) == "alte cheltuieli":
            if get_suma(cheltuiala) > tip["alte cheltuieli"]:
                tip["alte cheltuieli"] = get_suma(cheltuiala)
    if chelt_tip == "intretinere":
        return tip["intretinere"]
    elif chelt_tip == "canal":
        return tip["canal"]
    elif chelt_tip == "alte cheltuieli":
        return tip["alte cheltuieli"]
    return None