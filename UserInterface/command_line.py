from Domain.cheltuiala import get_str
from Logic.CRUD import create, delete


def handle_add(lst_cheltuieli, param):
    """
    Adauga in lista cheltuiala
    :param lst_cheltuieli: lsita de cheltuieli
    :param param: o lista ce contine parametrii cheltuielii
    :return: lista de cheltuieli cu cheltuiala adaugata, in caz contrar returneaza lista de cheltuieli
    """
    try:
        if len(param) != 6:
            raise ValueError("Numar invalid de parametrii")
        id_carte = int(param[1])
        nr_apartament = param[2]
        suma = param[3]
        data = param[4]
        tip = param[5]
        return create(lst_cheltuieli, id_carte, nr_apartament, suma, data, tip, [], [])
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
        new_cheltuieli = delete(lst_cheltuieli, int(param[1]), [], [])
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

        command = input("Introduceri comanda dorita(se pot adauga mai multe prin separatorul ',' : ")
        commands = command.split(",")
        for command in commands:

            lst = command.split()

            if lst[0] == "add":
                cheltuieli = handle_add(cheltuieli, lst)
            elif lst[0] == "show_all":
                handle_show_all(cheltuieli)
            elif lst[0] == "delete":
                cheltuieli = handle_delete(cheltuieli, lst)
            elif lst[0] == "Exit":
                return 0
            else:
                print("Comanda invalida!")
