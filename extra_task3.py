# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
print('--------------------------------')
print('Задание 1')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
names = dict()
for lstudent in students:
    lname = lstudent['first_name']
    names[lname] = 1 + names.get(lname,0)
for key, value in names.items():
  print(f'{key}: {value}')

  # Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
print('--------------------------------')
print('Задание 2')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
names = dict()
for lstudent in students:
    lname = lstudent['first_name']
    names[lname] = 1 + names.get(lname,0)
maxval=0
for key, value in names.items():
  if value > maxval:
    maxkey = key
    maxval = value
print(f'Самое часто имя среди учеников: {maxkey}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
print('--------------------------------')
print('Задание 3')
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
classnum = 0
for lclass in school_students:
  classnum += 1
  names = dict()
  for lstudent in lclass:
    lname = lstudent['first_name']
    names[lname] = 1 + names.get(lname,0)
  maxval=0
  for key, value in names.items():
    if value > maxval:
      maxkey = key
      maxval = value
  print(f'Самое частое имя в классе {classnum}: {maxkey}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
print('--------------------------------')
print('Задание 4')
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for lclass in school:
  lclass['sex'] = {'boys':0,'girls':0}
  for lstudent in lclass['students']:
    if is_male.get(lstudent['first_name']):
      lclass['sex']['boys'] += 1 
    else:
      lclass['sex']['girls'] += 1 
  print('В классе {cl} {girl} девочки и {boy} мальчика'.format(cl=lclass['class'],girl=lclass['sex']['girls'],boy=lclass['sex']['boys']))

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
print('--------------------------------')
print('Задание 5')
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
genders = [
  {'gender':'boys','maxcnt':0,'maxclass':'','rugender':'мальчиков'},
  {'gender':'girls','maxcnt':0,'maxclass':'','rugender':'девочек'}
]
for lclass in school:
  lclass['sex'] = {'boys':0,'girls':0}
  for lstudent in lclass['students']:
    if is_male.get(lstudent['first_name']):
      lclass['sex']['boys'] += 1
    else:
      lclass['sex']['girls'] += 1
  for lgender in genders:
    if lgender['maxcnt'] < lclass['sex'][lgender['gender']]:
      lgender['maxcnt'] = lclass['sex'][lgender['gender']]
      lgender['maxclass'] = lclass['class']
for lgender in genders:
    print('Больше всего {rug} в классе {cl}'.format(rug=lgender['rugender'],cl=lgender['maxclass']))
  
  #if maxgender['maxb'] < lclass['sex']['boys']:
    #maxgender['maxb'] = lclass['sex']['boys']
    #maxgender['maxbclass'] = lclass['class']
  #if maxgender['maxg'] < lclass['sex']['girls']:
    #maxgender['maxg'] = lclass['sex']['girls']
    #maxgender['maxgclass'] = lclass['class']


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a