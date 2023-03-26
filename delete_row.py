import csv
import os


def delete_row(bd, rows_numbers):
    #Получает на вход адрес Базы даных и список ID строк, которые нужно удалить из Базы данных, ничего не возвращает
    existing = []
    with open(bd, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='|')
        headers = reader.fieldnames
        for row in reader:
            if row['id'] not in rows_numbers:
                existing.append(row)
            else:
                print('Удалена строка  c ID: ', row['id'] , '\n')
        f.close
    with open(bd, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, delimiter='|', fieldnames=headers)
        writer.writeheader()
        writer.writerows(existing)
        f.close