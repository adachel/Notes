import datetime
import json

def create_or_add_note(name_note, text_note):  # создать или добавить заметку
    db = datetime.datetime.now()
    current_time = db.strftime('%d.%m.%Y %H:%M:%S')
    try:
        with open('data.json', encoding='utf-8') as file:
            file_content = file.read()
            templates = json.loads(file_content)
            last_elem = templates[-1]
            count = last_elem.get("Id", 0)
            note = {"Id": count + 1, "time": current_time, "name": name_note, "text": text_note}
            templates.append(note)

        with open('data.json', 'w', encoding='utf-8') as file:
            for i in range(len(templates)):
                if i == 0:
                    file.write(f'[{json.dumps(templates[i], ensure_ascii=False)},\n')
                elif i == len(templates) - 1:
                    file.write(f'{json.dumps(templates[i], ensure_ascii=False)}]\n')
                else:
                    file.write(f'{json.dumps(templates[i], ensure_ascii=False)},\n')
    except:
        new_note = [{"Id": 1, "time": current_time, "name": name_note, "text": text_note}]
        with open('data.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(new_note, ensure_ascii=False))


def list_note():  # список заметоk
    try:
        with open('data.json', encoding='utf-8') as file:
            file_content = file.read()
            templates = json.loads(file_content)

        sort_templates = sorted(templates, key=lambda temp: temp["time"], reverse=True)

        for i in range(len(sort_templates)):
            print(f"Id: {sort_templates[i]["Id"]}; "
                  f"время записи: {sort_templates[i]["time"]}; "
                  f"наименование: {sort_templates[i]["name"]}")
    except:
        print("Заметок нет")


def read_note(): # чтение заметки
    search_note = ""
    try:
        with open('data.json', encoding='utf-8') as file:
            file_content = file.read()
            templates = json.loads(file_content)

        note_id = int(input("Введите Id заметки\n"))

        for i in range(len(templates)):
            if (note_id == templates[i]["Id"]):
                time_create = templates[i]["time"]
                name_note = templates[i]["name"]
                text = templates[i]["text"]
                search_note = (f"Время создания или изменения заметки - {time_create},"
                               f"\nНаименование заметки - {name_note},"
                               f"\nТекст заметки:\n{text}\n")
                break
            else: search_note = "Такой заметки нет"
        print(search_note)
    except: print("Заметок нет")


def edit_note(): # Изменить заметку
    db = datetime.datetime.now()
    current_time = db.strftime('%d.%m.%Y %H:%M:%S')
    try:
        with open('data.json', encoding='utf-8') as file:
            file_content = file.read()
            templates = json.loads(file_content)

        note_id = int(input("Введите Id заметки\n"))

        for i in range(len(templates)):
            if (note_id == templates[i]["Id"]):
                text = templates[i]["text"]
                print(f"Текущий текст\n{text}")
                print("Введите новый текст")
                new_text = input()
                templates[i]["text"] = new_text
                templates[i]["time"] = current_time
                with open('data.json', 'w', encoding='utf-8') as file:
                    for i in range(len(templates)):
                        if i == 0:
                            file.write(f'[{json.dumps(templates[i], ensure_ascii=False)},\n')
                        elif i == len(templates) - 1:
                            file.write(f'{json.dumps(templates[i], ensure_ascii=False)}]\n')
                        else:
                            file.write(f'{json.dumps(templates[i], ensure_ascii=False)},\n')
    except:
        print("Заметок нет")


def select_date(): # Выбрать заметки по дате
    try:
        with open('data.json', encoding='utf-8') as file:
            file_content = file.read()
            templates = json.loads(file_content)

        date = input("Введите дату в формате дд.мм.гггг\n")

        for i in range(len(templates)):
            if (date == templates[i]["time"][:10]):
                note = templates[i]
                print(note)
    except:
        print("Заметок нет")


def delete_note(): # Удалить заметку
    try:
        with open('data.json', encoding='utf-8') as file:
            file_content = file.read()
            templates = json.loads(file_content)

        note_id = int(input("Введите Id удаляемой заметки\n"))

        for i in range(len(templates)):
            if (note_id == templates[i]["Id"]):
                templates.pop(i)
                with open('data.json', 'w', encoding='utf-8') as file:
                    for i in range(len(templates)):
                        if i == 0:
                            file.write(f'[{json.dumps(templates[i], ensure_ascii=False)},\n')
                        elif i == len(templates) - 1:
                            file.write(f'{json.dumps(templates[i], ensure_ascii=False)}]\n')
                        else:
                            file.write(f'{json.dumps(templates[i], ensure_ascii=False)},\n')
    except:
        print("Заметок нет")


def menu_notes():
    print("Приложение ЗАМЕТКИ")
    print("Выберите действие")
    while True:
        ch = int(input("1 - Создать или добавить заметку, "
                       "2 - Просмотр списка заметок, "
                       "3 - Просмотр заметки, "
                       "4 - Изменить заметку, "
                       "5 - Выбрать заметки по дате, "
                       "6 - Удалить заметку, "
                       "0 - Выход из программы\n"))
        match ch:
            case 1: # Создать или добавить заметку
                name_note = input("Название заметки\n")
                text_note = input("Текст заметки\n")
                create_or_add_note(name_note, text_note)
                continue
            case 2: # Просмотр списка заметок
                list_note()
                continue
            case 3: # Просмотр заметки
                read_note()
                continue
            case 4: # Изменить заметку
                edit_note()
                continue
            case 5:
                select_date()
                continue
            case 6: # Удалить заметку
                delete_note()
                continue
            case 0: # Выход из программы
                print("Выход из программы")
                break

menu_notes()