"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""

import datetime
#import dateutil

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    fmask = '%d.%m.%Y %H:%M'
    #сегодня
    current_date = datetime.datetime.now()
    print(current_date.strftime(fmask))
    #вчера
    print((current_date - datetime.timedelta(days=1)).strftime(fmask))
    #сегодняшнее число месяца
    current_day = int(current_date.strftime('%d'))
    #первый день текущего месяца
    first_day_of_current_month = current_date.replace(day=1)
    #последний день предыдущего месяца
    last_day_of_previous_month = first_day_of_current_month - datetime.timedelta(days=1)
    #месяц назад
    try:
        last_month = last_day_of_previous_month.replace(day=current_day)
    except ValueError:
        last_month = last_day_of_previous_month
    print(last_month.strftime(fmask))
    




def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.datetime.strptime(string, '%m/%d/%y %H:%M:%S.%f')
    
if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
