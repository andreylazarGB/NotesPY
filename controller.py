import model
import text
import view
from datetime import datetime


def search_note():
    word = view.input_request(text.input_search_word)
    result = model.find_note(word)
    view.show_book(result, text.not_find(word))
    if result:
        return True

def start():
    while True:
        choice = view.main_menu()
        if choice == 1:
            model.open_file()
            view.print_message(text.load_successful)
        if choice == 2:
            model.save_file()
            view.print_message(text.save_successful)
        if choice == 3:
            model.sort_file()
            view.show_book(model.notes_book, text.empty_book_error)
        if choice == 4:
            new_note = view.input_note(text.input_note)
            today = datetime.now()
            new_note.append(today.strftime("%Y-%m-%d %H:%M:%S"))
            model.add_note(new_note)
            view.print_message(text.note_action(new_note[0], text.operation[0]))

        if choice == 5:
            search_note()
        if choice == 6:
            if search_note():
                c_id = int(view.input_request(text.input_edit_note_id))
                new_note = view.input_note(text.input_edit_note)
                today = datetime.now()
                new_note.append(today.strftime("%Y-%m-%d %H:%M:%S"))
                name = model.edit_note(c_id, new_note)
                view.print_message(text.note_action(name, text.operation[1]))
        if choice == 7:
            if search_note():
                c_id = int(view.input_request(text.input_dell_note_id))
                name = model.delete_note(c_id)
                view.print_message(text.note_action(name, text.operation[2]))

        if choice == 8:
            view.print_message(text.exit_program)
            break
