from Domain.cheltuiala import get_suma, get_tip


def cea_mai_mare_cheltuiala_tip(lst_cheltuieli, chelt_tip):
    tip = {
        "intretinere": 0,
        "canal": 0,
        "alte cheltuieli": 0
    }
    for cheltuiala in lst_cheltuieli:
        if get_tip(cheltuiala) == "intretinere":
            tip["intretinere"] = get_suma(cheltuiala)
        if get_tip(cheltuiala) == "canal":
            tip["canal"] = get_suma(cheltuiala)
        if get_tip(cheltuiala) == "alte cheltuieli":
            tip["alte cheltuieli"] = get_suma(cheltuiala)
    if chelt_tip == "intretinere":
        return tip["intretinere"]
    elif chelt_tip == "canal":
        return tip["canal"]
    elif chelt_tip == "alte cheltuieli":
        return tip["alte cheltuieli"]
