from Domain.cheltuiala import get_suma, get_data, get_tip, get_nr_apartament, get_str, creeaza_cheltuiala, get_id
from Logic.CRUD import create, update, read, delete


def show_menu():
    print('1.CRUD')
    print('x.Exit')


def handle_add(cheltuieli):
    id_apartament = int(input('Dati id-ul apartamentului: '))
    ok = 0
    for cheltuiala in cheltuieli:
        if get_id(cheltuiala) == id_apartament:
            ok = ok + 1
    if ok == len(cheltuieli):
        print("Apartament cu acest id deja exista")
    else:
        nr_apartament = int(input('Dati numarul apartamentului: '))
        suma = float(input('Dati suma cheltuielii: '))
        data = input('Introduceti data in formatul DD/MM/YYYY: ')
        tip = input('Introduceti tip-ul cheltuielii ')
        return create(cheltuieli, id_apartament, nr_apartament, suma, data, tip)


def handle_update(cheltuieli):
    id_apartament = int(input("Dati id-ul apartamentului ce ii trebuie modificata cheltuiala: "))
    # daca l ai pus inainte nu face figuri ,iar daca l ai pus face
    nr_apartament = int(input('Dati noul numarul  a apartamentului: '))
    suma = float(input('Dati noua suma: '))
    data = input("Introduceti data in formatul DD/MM/YYYY: ")
    tip = input('Dati noul tip: ')
    return update(cheltuieli, creeaza_cheltuiala(id_apartament, nr_apartament, suma, data, tip))


def handle_delete(cheltuieli):
    id_apartament = int(input('Dati id-ul apartamentului pentru stergere: '))
    ok = 0
    for cheltuiala in cheltuieli:
        if get_id(cheltuiala) != id_apartament:
            ok = ok + 1
    if ok == len(cheltuieli):
        print("Nu exista acest id")
    else:
        cheltuieli = delete(cheltuieli, id_apartament)
        print('S-a efectuat stergerea')
        return cheltuieli


def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_show_details(cheltuieli):
    id_apartament = int(input('Dati id-ul apartamentului pentru detalii: '))
    ok = 0
    for chelt in cheltuieli:
        if get_id(chelt) != id_apartament:
            ok = ok + 1
    if ok == len(cheltuieli):
        print("Nu este niciun apartament cu acest id")
    else:
        cheltuiala = read(cheltuieli, id_apartament)
        print('Numarul apartamentului este: {}'.format(get_nr_apartament(cheltuiala)))
        print('Suma ce trebuie cheltuita este: {}'.format(get_suma(cheltuiala)))
        print('Data la care s-au generat costurile: {}'.format(get_data(cheltuiala)))
        print('Tipul cheltuielii este: {}'.format(get_tip(cheltuiala)))


def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii cheltuiala')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return cheltuieli


def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return cheltuieli
