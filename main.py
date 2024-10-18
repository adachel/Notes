import json
import datetime

def Create_or_Add_Note(name_note, text_note):
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

        with open('data.json', 'w', encoding= 'utf-8') as file:
            json.dump(templates, file, ensure_ascii=False)

    except:
        new_note = [{"Id": 1, "time": current_time, "name": name_note, "text": text_note}]
        with open('data.json', 'w', encoding= 'utf-8') as file:
            json.dump(new_note, file, ensure_ascii=False)

def List_Note():
    with open('data.json', encoding= 'utf-8') as file:
        file_content = file.read()
        templates = json.loads(file_content)

    for i in range(len(templates)):
        print(f"Id: {templates[i]["Id"]}; время: {templates[i]["time"]}; наименование: {templates[i]["name"]}")


def Read_Note(Id = 0, name = ""):
    with open('data.json', encoding='utf-8') as file:
        file_content = file.read()
        templates = json.loads(file_content)

    for i in range(len(templates)):
        if(Id == templates[i]["Id"] or name == templates[i]["name"]):
            print(f"текст заметки: {templates[i]["text"]}")




# name_note = input("Название заметки\n")
# text_note = input("Текст заметки\n")
#
# Create_or_Add_Note(name_note, text_note)

# List_Note()

Read_Note("первая")




















