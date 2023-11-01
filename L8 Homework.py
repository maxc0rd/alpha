# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.
# ???
# my_list = ['abc', 'def', 'ghi', 'jkl', 'mno']
# # new_list = []
# new_list = []
# print(new_list)
# # print(len(my_list[1::2]))
# for x in range(len(my_list)):
#     new_list.append(x)


# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".
#
# my_list = ['abc', 'def', 'ass', 'jkl', 'mno']
#
# new_list = [t for t in my_list if t[0] == "a"]
# print(new_list)

# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.
#
# my_list = ['jazz', 'quiz', 'ass', 'bla', 'mno']
#
# new_list = [t for t in my_list if "a" in t]
# print(new_list)

# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]
#
# list_dict = [
#     {
#         "name": "Liam",
#         "age": 29
#     },
#     {
#         "name": "Keith",
#         "age": 36
#     },
#     {
#         "name": "Leeroy",
#         "age": 44
#     }
# ]
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.
#

# new_list = []
# final_list = []
#
# for n in list_dict:
#     for m in n.values():
#         if type(m) is int:
#             new_list.append(m)
#     if n["age"] == min(new_list):
#         final_list.append(n["name"])
# print(final_list)

# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
#
# final_list = []
# new_dict = {}
#
# for n in list_dict:
#     for m in n.values():
#         if type(m) is str:
#             new_dict.update({m: len(m)})
#
# for key in new_dict.items():
#     if key[1] == max(new_dict.values()):
#         final_list.append(key)
# print(final_list)

# в) Порахувати середню вік усіх людей із початкового списку.
#
# new_list = []
#
# var = float(0)
# for n in list_dict:
#     for m in n.values():
#         if type(m) is int:
#             new_list.append(m)
# print(sum(new_list) / len(new_list))

# 5) Дано два словники my_dict_1 і my_dict_2.
#
my_dict_1 = {
    "firstname": "John",
    "lastname": "Doe",
    "country": "UK"
}

my_dict_2 = {
    "firstname": "Ben",
    "lastname": "Kingsly",
    "city": "London"
}

# а) Створити список із ключів, які є в обох словниках.
#
# Вариант 1:
#
# my_list = []
#
# for match in my_dict_1:
#     if match in my_dict_2:
#         my_list.append(match)
#
# print(my_list)

# Вариант 2:
#
# my_list = []
#
# my_list.append(my_dict_1.keys() - (my_dict_1.keys() - my_dict_2.keys()))
# print(my_list)

# б) Створити список із ключів, які є у першому, але немає у другому словнику.
#
# my_list = []
#
# my_list.append((my_dict_1.keys() - my_dict_2.keys()))
# print(my_list)

# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
#
# some_dict = {}
#
# for x, y in my_dict_1.items():
#     if x not in my_dict_2:
#         some_dict.update({x: y})
#
# print(some_dict)

# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помістити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
#
some_dict = {}

for a, b in my_dict_1.items():
    if a in my_dict_2:
        some_dict.update({a: b})
# print(some_dict)
        for c, d in my_dict_2.items():
            if c not in my_dict_1:

#         for c, d in my_dict_2.items():
#             if c in my_dict_1:
#                 some_dict.update({c: d+b})
#
# print(some_dict)

# + -
# some_dict = {}
#
# for a, b in my_dict_1.items():
#     if a not in my_dict_2:
#         some_dict.update({a: b})
#         for c, d in my_dict_2.items():
#             if c in my_dict_1:
#                 some_dict.update({c: d+b})
#
# print(some_dict)


# for match in str1:
#     if match in str2 and str1.count(match) == 1 and str2.count(match) == 1:
#         my_list.append(match)
# print(my_list)