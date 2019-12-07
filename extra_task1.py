# Вывести последнюю букву в слове
print('--------------------------------')
print('Задание 1')
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
print('--------------------------------')
print('Задание 2')
word = 'Архангельск'
print(sum([word.lower().count(x) for x in "а"]))

# Вывести количество гласных букв в слове
print('--------------------------------')
print('Задание 3')
word = 'Архангельск'
print(sum([word.lower().count(x) for x in "аеёиоуыэюя"]))

# Вывести количество слов в предложении
print('--------------------------------')
print('Задание 4')
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
print('--------------------------------')
print('Задание 5')
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова.
print('--------------------------------')
print('Задание 6')
sentence = 'Мы приехали в гости'
total_len = 0
word_list = sentence.split()
for word in word_list:
    total_len += len(word)
try:
    print(total_len/len(sentence.split()))
except:print(0)