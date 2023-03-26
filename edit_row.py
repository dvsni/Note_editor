import csv
import checkers


def modify_row(bd, id_key, field, new_value):
    #Получает на вход: адрес Базы данных, ключ строки, имя поля к изменению, новое значение поля
    existing = []
    with open(bd, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='|')
        headers = reader.fieldnames
        for row in reader:
            existing.append(row)
        for row in existing:
            if row['id'] == id_key:
                row[field] = new_value
                row['date'] = checkers.timestamp()
    with open(bd, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, delimiter='|', fieldnames=headers)
        writer.writeheader()
        writer.writerows(existing)