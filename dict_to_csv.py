"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    my_list = [ {"name":"Иванов","age":45,"job":"Инженер"},
                {"name":"Петров","age":57,"job":"Грузчик"},
                {"name":"Сидоров","age":60,"job":"Охранник"},
                {"name":"Алексеев","age":32,"job":"Водитель"},
                {"name":"Медведев","age":25,"job":"Строитель"}
    ] 
    
    with open('my_list.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ["name","age","job"]
        writer = csv.DictWriter(f,fields,delimiter=';')
        writer.writeheader()
        for i in my_list:
            writer.writerow(i)


if __name__ == "__main__":
    main()
