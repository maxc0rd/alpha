# Ви маєте змінну my_str, тип - str. Надрукувати ЧИСЛО скільки РІЗНИХ символів зустрічається в my_str.
# Велика та маленька літера вважається одним символом. Пробіл, коми і т.д. вважаємо також як символи.
# Наприклад: my_str="bla BLA car"
#            Виведення на екран: 6
#
# my_str = "Good Day!"
# my_list = []
#
# temp_list = list(my_str.lower())
# # print(temp_list)
# for i in temp_list:
#     if i not in my_list:
#         my_list.append(i)
# print(len(my_list))

# Ви маєте змінну my_str, та порожній список my_list. Заповнити my_list УНІКАЛЬНИМИ символами з my_str.
# Велика та маленька літера вважається одним символом. Пробіл, коми і т.д. вважаємо також як символи.
# Наприклад: my_str = "bla BLA car"
#            Виведення на екран: ["b", "l", "a", " ", "c", "r"]
#
# my_str = "Good Day!"
# my_list = []
#
# temp_list = list(my_str.lower())
# # print(temp_list)
# for i in temp_list:
#     if i not in my_list:
#         my_list.append(i)
# print(my_list)

# Дано рядок my_str та порожній список my_list. Заповнити my_list символами з my_str,
# які стоять на парних місцях у рядку (вважаємо з 0)
# Наприклад: my_str = "bla BLA car"
#            Виведення на екран: ["b", "a", "B", "A", "c", "r"]
#
# my_str = "good morning"
# my_list = []
#
# for i in my_str[::2]:
#     my_list.append(i)
# print(my_list)

# Дано рядок my_str, список str_index цілих чисел в діапазоні від 0 до довжини рядка мінус 1, пустий список my_list.
# Заповнити my_list символами my_str, які стоять на місцях з індексами із str_index
# Наприклад: my_str = "bla BLA car"
#            my_list = [0, 2, 4, 4, 8]
#            Виведення на екран: ["b", "a", "B", "B", "c"]
#
#
# Дано ціле число (int). Визначити скільки цифр у цьому числі.
# Наприклад: my_number = 228989
#            Виведення на екран: 6
#
# number = 435801
# my_list = []
#
# for i in str(number):
#     if i.isdigit() is True:
#         my_list.append(i)
# print(len(my_list))

# Дано ціле число. Визначити найбільшу цифру у цьому числі.
# Наприклад: my_number = 228989
#            Виведення на екран: 9
#
# number = 7612934
#
# print(sorted(str(number))[-1])

# Дано ціле число. Скласти число (int) із цифрами у зворотному порядку.
# Наприклад: my_number = 123
#            Виведення на екран: 321

# number = 632
# mod_number = str(number)[::-1]
# mod_number_int = int(mod_number)
# print(mod_number_int)

# Дано ціле число. Скласти число з цифрами в порядку зростання (зменшення).
# Наприклад: my_number = 3254
#            Виведення на екран: 2345   #зростання
#            Виведення на екран: 5432   #зменшення
#
# number = 756201
#
# number_incr = "".join(sorted(str(number)))
# number_decr = "".join(sorted(str(number), reverse=True))
#
# print(number_incr)
# print(number_decr)

# Дано списки my_list_1 та my_list_2. Створити список my_result в який помістити елементи
# з my_list_1 та my_list_2 через один, починаючи з my_list_1.
# a) кількість ел-тів однакове
# б) кількість ел-тів різне
# Наприклад: my_list_1 = [1, 2, 3]
#            my_list_2 = [10, 20, 30] # для варінту a
#            my_list_2 = [10, 20, 30, 40] # для варінту б
#            Виведення на екран: [1, 10, 2, 20, 3, 30]   #ел-тів однакове
#            Виведення на екран: [1, 10, 2, 20, 3, 30, 40]   #ел-тів різне