from Domain.cheltuiala import get_suma, get_data, get_tip, get_nr_apartament, get_str, creeaza_cheltuiala, get_id
from Logic.CRUD import create, update, read, delete
from Logic.Cel_mai_mare_tip import cea_mai_mare_cheltuiala_tip
from Logic.adunare_cheltuieli import adunare_cheltuieli
from Logic.ordonarea_cheltuielilor import ord_chelt_dupa_suma_desc
from Logic.suma_lunara import suma_lunara


def show_menu():
    print('1.CRUD')
    print('2.Adunarea unei valori la cheltuielile dintr-o anumita data')
    print('4.Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială')
    print('5.Ordonarea cheltuielilor descrescător după sumă')
    print('6.Suma pe luna')
    print('x.Exit')


def handle_add(cheltuieli):
    try:
        id_cheltuiala = int(input('Dati id-ul cheltuielii: '))
        nr_apartament = int(input('Dati numarul apartamentului: '))
        suma = float(input('Dati suma cheltuielii: '))
        data = input('Introduceti data in formatul DD/MM/YYYY: ')
        tip = input('Introduceti tip-ul cheltuielii ')
        return create(cheltuieli, id_cheltuiala, nr_apartament, suma, data, tip)
    except ValueError as va:
        print('Error: ', va)
    return cheltuieli


def handle_update(cheltuieli):
    try:
        id_cheltuiala = int(input("Dati id-ul cheltuielii ce ii trebuie modificata cheltuiala: "))
        nr_apartament = int(input('Dati noul numarul  a apartamentului: '))
        suma = float(input('Dati noua suma: '))
        data = input("Introduceti data in formatul DD-MM-YYYY: ")
        tip = input('Dati noul tip: ')
        return update(cheltuieli, creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tip))
    except ValueError as va:
        print('Error: ', va)
    return cheltuieli


def handle_delete(cheltuieli):
    try:
        id_cheltuieli = int(input('Dati id-ul cheltuielii pentru stergere: '))
        new_cheltuieli = delete(cheltuieli, id_cheltuieli)
        print("Stergerea s-a efectual cu succes")
        return new_cheltuieli
    except ValueError as va:
        print('Error:', va)
    return cheltuieli


def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_show_details(cheltuieli):
    id_cheltuieli = int(input('Dati id-ul cheltuielii pentru detalii: '))
    ok = 0
    for chelt in cheltuieli:
        if get_id(chelt) != id_cheltuieli:
            ok = ok + 1
    if ok == len(cheltuieli):
        print("Nu este niciun apartament cu acest id")
    else:
        cheltuiala = read(cheltuieli, id_cheltuieli)
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


def handle_adaugare(cheltuieli):
    valoare = float(input("Introduceti valoarea pe care vreti sa o adaugati la cheltuieli"))
    data = input("introduceti data la care sa se adauge valoarea")
    cheltuieli = adunare_cheltuieli(cheltuieli, valoare, data)
    return cheltuieli


def handle_tip(cheltuieli):
    while True:
        print('1.Cea mai mare suma de tip-ul  "intretinere": ')
        print('1.Cea mai mare suma de tip-ul  "canal": ')
        print('1.Cea mai mare suma de tip-ul  "alte cheltuieli" :')
        optiune = input("Optiunea aleasa: ")
        if optiune == '1':
            tip = cea_mai_mare_cheltuiala_tip(cheltuieli, "intretinere")
            print(tip)
        elif optiune == '2':
            tip = cea_mai_mare_cheltuiala_tip(cheltuieli, "canal")
            print(tip)
        elif optiune == '3':
            tip = cea_mai_mare_cheltuiala_tip(cheltuieli, "alte cheltuieli")
            print(tip)
        elif optiune == 'b':
            break
        else:
            print("Optiune invalida")
    return cheltuieli


def handle_ordo(cheltuieli):
    new_list = ord_chelt_dupa_suma_desc(cheltuieli)
    print(new_list)

def handle_suma_luni(cheltuieli):
    lst = suma_lunara(cheltuieli)
    for luna in lst:
        print(f"In luna a {luna} sumele cheltuielilor sunt: {lst[luna]}")
def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        if optiune == '2':
            cheltuieli = handle_adaugare(cheltuieli)
        elif optiune == '4':
            cheltuieli = handle_tip(cheltuieli)
        elif optiune == '5':
            cheltuieli = handle_ordo(cheltuieli)
        elif optiune == '6':
             handle_suma_luni(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return cheltuieli
