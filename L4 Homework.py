# 1) У вас є змінна величина, тип - int. Напишіть тернарний оператор для змінної new_value за таким правилом: якщо
#     значення менше 100, то new_value дорівнює половині значення, у протилежному випадку - протиположне
#     значенню число
# ------
По-моему, тут не совсем корректна формулировка задачи (допускаю, что это сделано специально :)).
Условие задания говорит, что "в противоположном случае" (то есть value > 100 будет противоположным
неравенству value < 100 ) переменная new_value должна иметь противоположное значение, но ничего не говорится о случае,
если будет значение 100.

Поэтому в Варианте 1 я использовал built-in функцию abs со знаком "-".

А в Варианте 2 попробовал впихнуть два условия в тернарный оператор (nested if), чтобы
выполнялось условие ("... в противоположном случае"), но читабельность кода сильно снижается :(

В Варианте 0 просто стоит знак минус перед value  ( но скучно :) )
# Вариант 0:
# value = 120
# new_value=value / 2 if value < 100 else -value
# print(new_value)
# #
# # Вариант 1:
# value = -120
# new_value=value / 2 if value < 100 else -abs(value)
# print(new_value)
# #
# # Вариант 2:
# value = 100
# new_value = 100 if value == 100 else value/2 if value < 100 else -value
# print(new_value)

# 2) У вас є змінна величина, тип - int. Написати тернарний оператор для змінної new_value за таким правилом: якщо
#     значення менше 100, то new_value дорівнює 1, у протилежному випадку - 0
#---------------
#
# Тут и далее исходил из того, что имеется ввиду "в любом другом случае", а не "в противоположном"
#
# value = 500
# new_value = 1 if value < 100 else 0
# print(new_value)

# 3) У вас є змінна величина, тип - int. Напишіть тернарний оператор для змінного new_value за таким правилом: якщо
#     значення менше 100, то new_value дорівнює True, у протилежному випадку - False
#---------------
# value = 140
# new_value = True if value < 100 else False
# print(new_value)

# 4) У вас є змінна my_str, тип - str. Якщо її довше менше 5, то допишіть в кінці строки її ж.
#     Приклад: було - "qwer", стало - "qwerqwer". Якщо довжина не менше 5, то залишити строку як є.
#---------------

# my_str = '1234'
# print(2 * my_str) if len(my_str) < 5 else print (my_str)

# 5) У вас є змінна my_str, тип - str. Якщо її довжина менше 5, то допишіть в кінці рядка перевернуту її ж.
#     Приклад: було - "qwer", стало - "qwerrewq". Якщо довжина не менше 5, то залишити строку як є.
#---------------

# my_str = '12345'
# print(my_str + my_str[::-1]) if len(my_str) < 5 else print (my_str)

# 6) Допрацювати завдання з калькулятором, щоб в кінці вичислення у користувача запитало, чи потрібен  калькулятор ще.
#   Якщо так, то запустити програму з початку.
# -----------
#
# print("\033[0;30;47m This TestCalc is made by Max Lekontsev in scope of Hillel's L3 homework.\033[0m")
# print("\n\033[0;30;47m All rights reserved :)\033[0m")
# operation = ''
# while operation != "q":
#     operation = input("\nEnter arithmetic operation you're going to calculate ('+', '-', '*' or '/')"
#                       "\nOtherwise, type 'q' to quit: ")
#     if operation == "+" or operation == "-" or operation == "*" or operation == "/":
#         first_number = ''
#         second_number = ''
#         first_no_error = ''
#         second_no_error = ''
#         result = 0
#         while not first_no_error:
#             try:
#                 first_number = float(input("\nPLEASE ENTER FIRST NUMBER: "))
#                 first_no_error = True
#             except ValueError:
#                 print("\n\033[1;31;40m :( Only numbers allowed!\033[0m")
#                 first_no_error = False
#         while second_no_error is not True or (operation == "/" and second_number == 0):
#             try:
#                 second_number = float(input("\nPLEASE ENTER SECOND NUMBER: "))
#                 if operation == "/" and second_number == 0:
#                     print("\n\033[1;31;40m ^_^ You can't divide by 0!\033[0m")
#                 else:
#                     pass
#                 second_no_error = True
#             except ValueError:
#                 print("\n\033[1;31;40m :( Only numbers allowed!\033[0m")
#                 second_no_error = False
#         # print("All good")
#         if operation == "+":
#             result = first_number + second_number
#         elif operation == "-":
#             result = first_number - second_number
#         elif operation == "*":
#             result = first_number * second_number
#         else:
#             result = first_number / second_number
#         print("\n\033[1;32;40m Your result: \033[0m" + str(result))
#     elif operation == "q":
#         print("\n\033[0;30;47m Thanks for using TestCalc. <3 Hugs and kisses <3\033[0m")
#     elif operation == "'+'" or operation == "'-'" or operation == "'*'" or operation == "'/'" or operation == "'q'":
#         print("\n\033[1;31;40m ;) Try without quotes.\033[0m")
#     else:
#         print("\n\033[1;31;40m ¯\_(ツ)_/¯ Sorry, currently TestCalc supports only 4 operations mentioned above.\033[0m")
