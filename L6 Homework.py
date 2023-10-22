# 1) У вас є список my_list із значеннями типу int. Роздрукувати значення, які більше 100.
#    Завдання виконати за допомогою циклу for.

my_list = [1, 100, 300, 4, 666, 21]
#
# for o in my_list:
#     if o > 100:
#         print(o)

# 2) У вас є список my_list зі значеннями типу int і порожній список my_results. Додати в my_results ті значення,
#    які більше 100. Роздрукувати список my_results. Завдання виконати за допомогою циклу for.

# my_list = [1, 100, 300, 4, 666, 21]
# my_results = []

# # Вариант 1:
#
# for o in my_list:
#     if o > 100:
#         my_results.append(o)
# if len(my_results) > 0:
#     print(my_results)
# else:
#     print("No numbers in the list that are greater than 100")

# # Вариант 2:
#
# for o in my_list:
#     if o > 100:
#         my_results.append(o)
# if not my_results:
#     print("No numbers in the list that are greater than 100")
# else:
#     print(my_results)

# 3) У вас є список my_list із значеннями типу int. Якщо my_list кількість елементів менше 2,
#    то в кінець додати значення 0. Якщо кількість елементів більша або дорівнює 2,
#    то додати суму останніх двох елементів. Кількість елементів у списку можна отримати за допомогою функції len(my_list)

# my_list = [1, 2, 3, 4]
#
# if len(my_list) < 2:
#     my_list.append(0)
# else:
#     my_list.append(my_list[-1]+my_list[-2])
# print(my_list)