# Промежуточная контрольная работа № 1 по блоку специализация.
# Информация о проекте:
# Необходимо написать проект, содержащий функционал работы с заметками. 
# Программа должна уметь:
# 1. создавать заметку
# 2. сохранять заметку
# 3. читать список заметок
# 4. редактировать заметку
# 5. удалять заметку.

import json

# Создание заметки.
def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    note = {"title": title, "content": content}
    return note

# Сохранение заметки в файл.
def save_note(note):
    with open("notes.json", "a") as f:
        f.write(json.dumps(note) + "\n")

# Чтение списка заметок из файла.
def read_notes():
    with open("notes.json", "r") as f:
        notes = [json.loads(line) for line in f]
    return notes

# Редактирование заметки.
def edit_note():
    notes = read_notes()
    title = input("Введите заголовок заметки для редактирования: ")
    for note in notes:
        if note["title"] == title:
            new_content = input("Введите новое содержимое заметки: ")
            note["content"] = new_content
            save_note(notes)
            print("Заметка отредактирована.")
            return
    print("Заметка не найдена.")

# Удаление заметки.
def delete_note():
    notes = read_notes()
    title = input("Введите заголовок заметки для удаления: ")
    for note in notes:
        if note["title"] == title:
            notes.delete_note(note)
            save_note(notes)
            print("Заметка удалена.")
            return
    print("Заметка не найдена.")

# Главное меню.
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из программы")
        choice = input("> ")

        if choice == "1":
            note = create_note()
            save_note(note)
            print("Заметка сохранена.")

        elif choice == "2":
            notes = read_notes()
            if not notes:
                print("Список заметок пуст.")
            else:
                print("Список заметок:")
                for note in notes:
                    print(f'{note["title"]}: {note["content"]}')

        elif choice == "3":
            edit_note()

        elif choice == "4":
            delete_note()

        elif choice == "5":
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()