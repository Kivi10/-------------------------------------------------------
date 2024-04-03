# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). 

import json
import os
import datetime

def create_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {'id': note_id, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно создана!")

def read_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Время создания: {note['timestamp']}")
        print(f"Текст заметки: {note['body']}")
        print()

def update_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок: ")
            note['body'] = input("Введите новый текст заметки: ")
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно обновлена!")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            return
    print("Заметка с указанным ID не найдена.")
    
def load_notes():
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as file:
            return json.load(file)
    return []

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Ваш выбор: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            update_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            return
        else:
            print("Некорректный выбор. Повторите.")

if __name__ == "__main__":
    main()