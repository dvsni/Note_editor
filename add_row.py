import os
import csv
import constants as const
from ui import *
from checkers import *
from datetime import time, date


def add_row(bd):
    # Принимает имя файла. Реализует добавление строки и заполнение её полей вводом значений через консоль позльзователем.
    # Ничего не возвращает, может пинговать об успешном добавлении в консоль
    new_note = ['']*4
    with open(bd, 'r+', newline='', encoding='utf-8') as f:
        reader_file = csv.reader(f, delimiter="|")
        new_note[0] = len(list(reader_file))+1
        writer_object = csv.writer(f, delimiter="|")
        new_note[1] = to_input('head')
        new_note[2] = to_input('body')
        new_note[3] = timestamp()
        writer_object.writerow(new_note)
    f.close()