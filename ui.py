from constants import ABILITIES
from checkers import check_menu_item as chk_menu
from checkers import checker_field
import csv
import constants
global headers
with open(constants.DATA_BASE_NAME) as f:
    reader = csv.reader(f, delimiter='|')
    headers = next(reader)

def get_action():
    # Ничего не принимает на вход. Вовзращает выбранное действие
    print('\n ')
    print(' Из списка ниже выберете желаемое действие: ')
    for item in ABILITIES:
        print(item)
    check = False
    while check == False:
        print('\n ')
        choise = input(' Ввыбор действия: ')
        check = chk_menu(choise)
        if check == False:
            print('Что-то невнятное. Попробуйте ввод ещё раз.')
    return choise

def agree(rows_list: list):
    # Принимает список ID строк, которые хотят удалить , возращает решение о том, удалять или нет- True или False
    dec = ''
    print('\n ')
    print(f' Точно удалить строки с ID {rows_list}?')
    while dec not in ('Y', 'N'):
        dec = input('Введите решение: Y = да, N=нет:  ')
        if dec not in ('Y', 'N'):
            print('Нераспознанное решение. Определись и ответь.\n')
    if dec in 'Y':
        return True
    if dec in 'N':
        return False

def row_to_modify(list_of_availible_rows):
    # Принимает список ключей, из которых можно выбрать ключ нужной строки, возвращает ключ выбранной строки
    while dec not in list_of_availible_rows:
        print('\n ')
        dec = input(
            ' Введите ключ строки(порядковый номер из первого столбца: )')
        if dec not in list_of_availible_rows:
            print('Нераспознанное решение. Определись и ответь.')
    return dec

def field_to_correct(db_name):
    # Принимает адрес базы данных, строку, возвращает имя заголовка поля, которое выбрано пользователем
    choice = ''
    with open(db_name) as f:
        reader = csv.reader(f, delimiter='|')
        headers = next(reader)
        print(headers)

    while choice not in headers:
        print('\n ')
        choice = input(' Введите наименование поля, которое нужно изменить:  ')
        if choice not in headers:
            print(' Нераспознанное поле. Определись и ответь.')
    return choice

def to_input(field):
    # Принимает имя поля, в которое будет внесено изменение строки, возвращает строку, которую нужно будет вставить вместо предыдущего значения
    value = ''

    if field == 'id':
        print('\n ')
        print(' Формат ввода: целое число, указывающее на ID строки')
    elif field in ('body', 'head'):
        print('\n ')
        if field == 'head':
            print(' Вводим заголовок заметки.')
        if field == 'body':
            print(' Вводим тело заметки.')
        print(' Формат ввода - строка длиной до 30 из буквенных символов.')

    chk = False
    value = input(' Введите значение ячейки: ')
    chk = checker_field(field, value)
    while chk == False:
        print('\n ')
        print(' Некорректный форамт ввода, пробуй ещё раз.')
        value = input(' Введите  значение ячейки: ')
        chk = checker_field(field, value)
    return value

def get_field_n_value():
    # Ничего не принимает,  запрашивает у пользователя поле для поиска и значение, 
    # которое нужно будет искать. Возвращает кортеж из двух элементов, где первый - поле, второе - значение
    f_n_v = ['', '']
    print('\n ')
    f_n_v[0] = input(' Укажите поле: ')
    while f_n_v[0] not in headers:
        f_n_v[0] = input(' Введите существующий заголовок поля: ')
    f_n_v[1] = to_input(f_n_v[0])
    return f_n_v

def get_id(bd):
    #Получает на вход адрес Базы данных. Запрашивает ID строки, в которой нужно будет заменять значение поля.
    # Проверяет на валидность. Возвращает id
    input_id = input(
        'Введите id строки, в которой хотите редактировать строку:')
    with open(bd) as f:
        reader = csv.reader(f, delimiter='|')
        id_list = [x[0] for x in reader]
    while input_id not in id_list or input_id == id_list[0]:
        input_id = input(
            f'Не существующий ID. \n Список существующих ID: {id_list[1:]} \n Попробуйте снова: ')
    return input_id

def ifempty_agree(id_list: list):
    if len(id_list) < 1:
        print('Не найдено ни одного элемента по критерию поиска')
        return False
    else:
        if agree(id_list) == True:
            return True
        else:
            print('Хорошо, удалять не будем')
            return False