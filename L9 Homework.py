# Для завданнь 1-7 за основу можете взяти код із попередніх ДЗ.
#
# 1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни.
#
# my_list = ["123", "abc", "456", "def"]
# new_list = []
#
#
# def revert_odd_symb(any_list):
#     for index in range(len(any_list)):
#         if index % 2 != 0:
#             new_list.append(any_list[index][::-1])
#         else:
#             new_list.append(any_list[index])
#
#     return new_list
#
#
# print(revert_odd_symb(my_list))

# 2. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".
#
# my_list = ["abc", "bbq", "aka", "ccc"]
# new_list = []
#
#
# def check_1st_symbol(any_list):
#
#     for symb in any_list:
#         if type(symb) is str and symb[0] == "a":
#             new_list.append(symb)
#
#     return new_list
#
#
# print(check_1st_symbol(my_list))

# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.
#
# my_list = ["abc", "baby", "kkk", "cd"]
# new_list = []
#
#
# def check_a_symbol(any_list):
#
#     for symb in any_list:
#         if "a" in symb:
#             new_list.append(symb)
#
#     return new_list
#
#
# print(check_a_symbol(my_list))

# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.
#
# my_list = ["abc", 22, "kkk", 45]
# new_list = []
#
#
# def only_strings(any_list):
#
#     for i in any_list:
#         if type(i) is str:
#             new_list.append(i)
#
#     return new_list
#
#
# print(only_strings(my_list))

# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.
#
# my_str = "abcab"
# new_list = []
#
#
# def unique_symbol(any_string):
#     for i in any_string:
#         if any_string.count(i) == 1:
#             new_list.append(i)
#
#     return new_list
#
#
# print(unique_symbol(my_str))

# 6. Написати функцію яка приймає один параметр - два рядки.
# Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.
#
# my_str1 = "aaaasdf1"
# my_str2 = "asdfff2"
# new_list = []
#
#
# def one_symb_match(string1, string2):
#     set1 = set(string1)
#     set2 = set(string2)
#     for match in set1:
#         if match in set2:
#             new_list.append(match)
#
#     return new_list
#
#
# print(one_symb_match(my_str1, my_str2))

# 7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.
#
# my_str1 = "Hello"
# my_str2 = "Hillel"
# new_list = []
#
#
# def one_symb_match(string1, string2):
#     for symbol in set(string1).intersection(set(string2)):
#         if string1.count(symbol) == 1 and string2.count(symbol) == 1:
#             new_list.append(symbol)
#
#     return  new_list
#
#
# print(one_symb_match(my_str1, my_str2))

# 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
#     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.
#
# Приклад використання функції:
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
#
# Відповідь: miller.249@sgdyyur.com