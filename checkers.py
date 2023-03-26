def check_menu_item(choise: str):
    # Принимает строку со значением
    # Возвращает bool - является ли входящая строка опцией меню
    check = False
    if choise in ('1', '2', '3', '4', '5', '6'):
        check = True
    return check


def checker_field(field: str, value: str):
    # Принимает: заголовок поля, значение, которое нужно проверить на соответствие 
    # формату поля возвращает Булеву функцию ИСТИНА\ЛОЖЬ на соответствие формату
    result = False
    if field == 'id':
        if value.isdigit() == True:
            result = True
    elif field in ('body', 'head'):
        if len(value) <= 300:
            result = True
    return result


def timestamp():
    #Ничего не принимает на вход, возвращает текущую отметку времени до секунд
    from datetime import datetime
    current_time = datetime.now()
    timestamp = current_time.timestamp()
    date_time = datetime.fromtimestamp(timestamp)
    str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
    return (str_date_time)