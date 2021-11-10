def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    Face operatia de undo
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :param current_list: lista curenta
    :return: lista dupa ce s-a efectuat operatia de undo, None - in caz ca nu exista functia de undo
    """
    if undo_list:
        top_undo = undo_list.pop()

        redo_list.append(current_list)
        return top_undo
    else:
        return current_list


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    Face operatia de redo
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :param current_list: Lista curenta
    :return: lista dupa ce s-a efectuat operatia de redo,None - in caz ca nu exista lista de redo
    """
    if redo_list:
        top_redo = redo_list.pop()

        undo_list.append(current_list)
        return top_redo
    else:
        return current_list
