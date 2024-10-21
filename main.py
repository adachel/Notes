import json
import datetime

def Create_or_Add_Note(name_note, text_note): # создать или добавить заметку
    db = datetime.datetime.now()
    current_time = db.strftime('%m.%d.%Y %H:%M')
    try:
        with open('data.json', encoding= 'utf-8') as file:
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


def List_Note(): # список заметоk
    with open('data.json', encoding= 'utf-8') as file:
        file_content = file.read()
        templates = json.loads(file_content)

    for i in range(len(templates)):
        print(f"Id: {templates[i]["Id"]}; время записи: {templates[i]["time"]}; наименование: {templates[i]["name"]}")


def Edit_Note(Id = 0, name = ""):
    try:
        with open('data.json', encoding='utf-8') as file:
            file_content = file.read()
            templates = json.loads(file_content)

        for i in range(len(templates)):
            if(Id == templates[i]["Id"] or name == templates[i]["name"]):
                text = templates[i]["text"]
                print(f"Текущий текст\n{text}")
                print("Введите новый текст")
                new_text = input()
                templates[i]["text"] = new_text
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






# name_note = input("Название заметки\n")
# text_note = input("Текст заметки\n")
#
# Create_or_Add_Note(name_note, text_note)

# List_Note()

Edit_Note(0, "первая")




















