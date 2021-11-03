from Domain.cheltuiala import get_str
from Logic.CRUD import create, delete


def handle_add(lst_cheltuieli, param):
    """
    Adauga in lista cheltuiala
    :param lst_cheltuieli: lsita de cheltuieli
    :param param: o lista ce contine parametrii cheltuielii
    :return: lista de cheltuieli cu cheltuiala adaugata, in caz contrar returneaza lista de cheltuieli
    """
    if len(param) != 6:
        raise ValueError("Nu ati introdus numarul exact de parametrii")
    try:
        print(param[1])
        return create(lst_cheltuieli, int(param[1]), param[2], param[3], param[4], param[5])
    except ValueError as ve:
        print("Error", ve)
    return lst_cheltuieli


def handle_delete(lst_cheltuieli, param):
    """
    Stergerea cheltuielii
    :param lst_cheltuieli: lista cu cheltuieli
    :param param: o lista ce contine parametrii cheltuielii
    :return: lista de cheltuieli cu cheltuiala stearsa, in caz contrar returneaza lista de cheltuieli
    """
    if len(param) != 2:
        raise ValueError("Nu ati introdus numarul exact de parametrii")
    try:
        new_cheltuieli = delete(lst_cheltuieli, int(param[1]))
        print("Stergerea s-a efectual cu succes")
        return new_cheltuieli
    except ValueError as va:
        print('Error:', va)
    return lst_cheltuieli


def handle_show_all(lst_cheltuieli):
    for cheltuiala in lst_cheltuieli:
        print(get_str(cheltuiala))


def show_menu():
    print("Introduceti comanda:")
    print("add [id_cheltuiala] [nr_apartament] [suma] [data] [tip]")
    print("delete [id_cheltuiala]")
    print("show_all")
    print("Exit")


def command_line(cheltuieli):
    show_menu()

    while True:
        command = input("Introduceti comanda:")
        comenzi = command.split(";")
        for comanda in comenzi:
            param = command.split()
            if comanda == 'show_all':
                handle_show_all(cheltuieli)
            elif param[0] == 'add':
                cheltuieli = handle_add(cheltuieli, param)
            elif param[0] == 'delete':
                cheltuieli = handle_delete(cheltuieli, param)
            elif param[0] == 'Exit':
                return 0
            else:
                print("Optiune invalida")
