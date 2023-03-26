import csv

def search(bd: str, field: str, value: str, type_output: int):
    # Принимает: Базу данных, поле, по которому будет производиться поиск, 
    # значение, по которому будет произовдиться поиск, тип вывода: 1 - вывести все строки, 
    # 2 - вывести идентификаторы найденных строк списком, возвращает список ID найденных строк
    with open(bd, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='|')
        headers = reader.fieldnames
        if type_output == 1:
            print('\n ')
            print('Найденные строки:')
            print(headers)
            for item in reader:
                if item[field] == value:
                    print(list(item.values()))
        elif type_output == 2:
            id_list = []
            for item in reader:
                if item[field] == value:
                    id_list.append(item['id'])
            return id_list
        else:
            print('Неизвестный режим работы функции')