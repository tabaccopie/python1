# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = [None, False, 12, 5.4, (1, 2), {'key1':1, 'key2':2}, [645, 'hh']]
for i in my_list:
    print(type(i))

# ==========================================================================
# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = input('Введите значения списка (через пробел): ')
my_list = list(my_list.split())

for i in range(1, len(my_list), 2):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]

print(f'Результат замены: %s' % my_list)

# ==========================================================================
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month = input('Введите месяц от 1 до 12: ')
if month.isdigit():
    month = int(month)
    list_month = ["Зима", "Весна", "Лето", "Осень"]
    dict_month = {0: "Зима", 1: "Весна", 2: "Лето", 3: "Осень"}
    if month in (1, 2, 12):
        print(f"Время года указанного месяца (из списка) %s" % list_month[0])
        print(f"Время года указанного месяца (из словаря) %s" % dict_month.get(0))
    elif month in (3, 4, 5):
        print(f"Время года указанного месяца (из списка) %s" % list_month[1])
        print(f"Время года указанного месяца (из словаря) %s" % dict_month.get(1))
    elif month in (6, 7, 8):
        print(f"Время года указанного месяца (из списка) %s" % list_month[2])
        print(f"Время года указанного месяца (из словаря) %s" % dict_month.get(2))
    elif month in (9, 10, 11):
        print(f"Время года указанного месяца (из списка) %s" % list_month[3])
        print(f"Время года указанного месяца (из словаря) %s" % dict_month.get(3))
else:
    print("Необходимо вводить число от 1 до 12!")



# ==========================================================================
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
my_list = input('Введите слова (через пробел): ')
my_list = list(my_list.split())
for i, word in enumerate(my_list, 1):
    print(i, word[:10])


# ==========================================================================
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
user_int = int(input('Введите натуральное число: '))
i = 0
if user_int > (max(my_list)):
    my_list.insert(0, user_int)
elif user_int < (min(my_list)):
    my_list.append(user_int)
else:
    for i in range(len(my_list)):
        if user_int == my_list[i]:
            my_list.insert((i+1), user_int)
            break
        elif user_int > my_list[i]:
            my_list.insert(i, user_int)
            break
print(f'Пользователь ввел число {user_int}. Результат: {my_list}')


# ===========================================================================================
# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
#
# }

key1 = input('Введите характеристику 1 из 4: ')
key2 = input('Введите характеристику 2 из 4: ')
key3 = input('Введите характеристику 3 из 4: ')
key4 = input('Введите характеристику 4 из 4: ')
num1 = int(input('Сколько товаров Вы хотите добавить?: '))
my_list = []
tmp_list1 = []
tmp_list2 = []
tmp_list3 = []
tmp_list4 = []
i = 1
while i <= num1:
    my_dict = ({key1: input(f'Введите {key1}: '), key2: input(f'Введите {key2}: '), key3: input(f'Введите {key3}: '),
                key4: input(f'Введите {key4}: ')})
    my_list.append((i, my_dict))
    tmp_list1.append(my_dict.get(key1))
    tmp_list2.append(my_dict.get(key2))
    tmp_list3.append(my_dict.get(key3))
    tmp_list4.append(my_dict.get(key4))
    i += 1


my_andict = dict({key1: tmp_list1, key2: tmp_list2, key3: tmp_list3, key4: set(tmp_list4)})
print(my_list)
print(my_andict)