class Note:
    def __init__(self):
        self.create_or_Add_Note()


    def create_or_Add_Note(self, name_note, text_note):  # создать или добавить заметку
        db = datetime.datetime.now()
        current_time = db.strftime('%m.%d.%Y %H:%M:%S')
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


    def list_Note(self):  # список заметоk
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


    def edit_Note(self, id=0, name=""):
        db = datetime.datetime.now()
        current_time = db.strftime('%m.%d.%Y %H:%M:%S')
        try:
            with open('data.json', encoding='utf-8') as file:
                file_content = file.read()
                templates = json.loads(file_content)

            for i in range(len(templates)):
                if (id == templates[i]["Id"] or name == templates[i]["name"]):
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