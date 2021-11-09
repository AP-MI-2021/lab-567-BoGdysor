from Tests.SORTARE_DESCRESCATOARE import test_ord_chelt_dupa_suma_desc
from Tests.TEST_ADUNARE_LA_CHELTUIELI import test_adunare_cheltuieli
from Tests.TEST_CEL_MAI_MARE_TIP import test_cea_mai_mare_cheltuiala_tip
from Tests.TEST_CRUD import test_crud
from Tests.TEST_SUMA_LUNI import test_suma_luni
from Tests.TEST_UNDO_REDO import test_undo_redo


def full_tests():
    test_adunare_cheltuieli()
    test_ord_chelt_dupa_suma_desc()
    test_cea_mai_mare_cheltuiala_tip()
    test_crud()
    test_suma_luni()
    test_undo_redo()