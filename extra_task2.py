# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки
print('--------------------------------')
print('Задание 1')
names = ['Оля', 'Петя', 'Вася', 'Маша']
for word in names:
    print(word)

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.
print('--------------------------------')
print('Задание 2')
names = ['Оля', 'Петя', 'Вася', 'Маша']
for word in names:
    print(f'{word} {len(word)}')

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика
print('--------------------------------')
print('Задание 3')
is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for word in names:
    sex  = 'м' if is_male.get(word) else 'ж'
    print(f'{word} {sex}')

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.
print('--------------------------------')
print('Задание 4')
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего групп: {len(groups)}')
for subgroups in groups:
    print(f'Учеников в группе {len(subgroups)}')

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша
print('--------------------------------')
print('Задание 5')
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
  [],
]
groupnum = 0
for subgroups in groups:
    groupnum += 1
    outpt_string = 'Группа ' + str(groupnum) + ': '
    for peoples in subgroups:
        outpt_string +=  peoples + ', '
    print(outpt_string.rstrip(', '))