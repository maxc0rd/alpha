# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.
#
# var = 12308000
#
# var_str = str(var)
# # Вариант 1:
#
# print(list(var_str).count("0"))
#
# # Вариант 2:
#
# zeros_list = []
# for symbol in var_str:
#     if symbol == "0":
#         zeros_list.append(symbol)
#
# print(zeros_list.count("0"))

# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі
#
# var = 100500
#
# var_str = str(var)
# # Вариант 1:
#
# zeros = len(var_str) - len(var_str.rstrip("0"))
# print(f"The number of zeros at the end is {zeros}")
#
# # Вариант 2:
#
# zero_list = []
# for zero in var_str[::-1]:
#     if zero != "0":
#         break
#     zero_list.append(zero)
#
# print(len(zero_list))

# 3. Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.
#
#
# Если под "четными местами" имеются ввиду четные индексы (0, 2, 4, ...), то:
#
# my_list_1 = ["a", "b", "c", "d", "e"]
# my_list_2 = ["1", "2", "3", "4", "5"]
# # Вариант 1:
#
# my_result = []
#
# my_result.extend(my_list_1[::2])
# my_result.extend(my_list_2[::2])
#
# print(my_result)

# # Вариант 2:
#
# my_result = my_list_1[::2]
# for i in my_list_2[::2]:
#     my_result.append(i)
# print(my_result)

# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]
#
# my_list = [1, 2, 3, 4]
#
# new_list = my_list.copy()
# temp = new_list.pop()
# temp2 = new_list.pop(0)
#
# new_list.insert(0, temp)
# new_list.append(temp2)

# print(new_list)

# 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)
#
# my_list = [1, 2, 3, 4]
#
# var = my_list.pop(0)
# my_list.append(var)
# print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)
#
# my_str = "43 більше ніж 34, але менше ніж 56"
# str2 = ""
# total = 0
# my_list = []
#
# my_str = my_str.split()
# for i in my_str:
#     if i.isdigit() is True:
#         my_str.pop(my_str.index(i)) and my_list.append(i)
#     else:
#         for n in i:
#             if n.isdigit() is True:
#                 str2 = str2 + n
# my_list.append(str2)
# for sum in my_list:
#     total = total + int(sum)
# print(total)

# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.
#
# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
# total = []
# for x in my_list[1:-1]:
#     if x > (my_list[my_list.index(x) - 1] + my_list[my_list.index(x) + 1]):
#         total.append(x)
# print(len(total))

# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.
#
# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
#
# for check in my_list:
#     if type(check) is str:
#         new_list.append(check)
# print(new_list)

# 9. Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.
#
# my_str = "Hello Hillel"
# my_list = []
#
# for x in my_str:
#     if my_str.count(x) == 1:
#         my_list.append(x)
#
# print(my_list)

# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.
#
# str1 = "Something"
# str2 = "Someone"
# my_list = []
#
# for match in str1:
#     if match in str2:
#         my_list.append(match)
# print(my_list)

# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу
#
# str1 = "aaaasdf1"
# str2 = "asdfff2"
# my_list = []
#
# for match in str1:
#     if match in str2 and str1.count(match) == 1 and str2.count(match) == 1:
#         my_list.append(match)
# print(my_list)
