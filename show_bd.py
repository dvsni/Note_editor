import csv

def show_all_bd(db_name):
    # Принимает на вход адрес Базы данных, выводит всю Базу данных в консоль, 
    # ничего не возвращает
    with open(db_name,newline='', encoding='utf-8') as f:
        reader = csv.reader(f,delimiter='|')
        headers = next(reader)
        print(headers)
        for row in reader:
            print(row)