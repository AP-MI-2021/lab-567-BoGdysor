def do_undo(undo_list: list, redo_list: list, current_list: list):
    if undo_list:
        top_undo = undo_list.pop()

        redo_list.append(current_list)
        return top_undo
    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    if redo_list:
        top_redo = redo_list.pop()

        undo_list.append(current_list)
        return top_redo
    return None
