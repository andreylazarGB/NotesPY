import datetime

PATH = 'notes.txt'
notes_book = {}


def open_file():
    global notes_book, PATH
    with open(PATH, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for i, note in enumerate(data, 1):  # начало enumerate  с 1
        note = note.strip().split(';')
        notes_book[i] = note


def sort_file():
    global notes_book
    data = []
    for note in notes_book.values():
        note = ';'.join(note)
        data.append(note)
    date_notes = list(map(lambda x: x.strip().split(';'), data))
    date_notes.sort(key=lambda x: x[1])
    for i, note in enumerate(date_notes, 1):  # начало enumerate  с 1
        notes_book[i] = note


def save_file():
    global notes_book, PATH
    data = []
    for note in notes_book.values():
        note = ';'.join(note)
        data.append(note)
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='utf-8') as file:
        file.write(data)


def add_note(new_note: list[str]):
    global notes_book
    c_id = max(notes_book) + 1
    notes_book[c_id] = new_note


def find_note(word: str) -> dict[int, list[str]]:
    global notes_book
    result = {}
    for c_id, note in notes_book.items():
        for field in note:
            if word.lower() in field.lower():
                result[c_id] = note
                break
    return result


def edit_note(c_id: int, new_note: list[str]):
    global notes_book
    current_note = notes_book.get(c_id)
    note = []
    for i in range(len(new_note)):
        if new_note[i]:
            note.append(new_note[i])
        else:
            note.append(current_note[i])
    notes_book[c_id] = note
    return note[0]


def delete_note(c_id: int) -> str:
    global notes_book
    return notes_book.pop(c_id)[0]
