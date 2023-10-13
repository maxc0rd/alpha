
# Calculator by Max Lekontsev
print("\033[0;30;47m This TestCalc is made by Max Lekontsev in scope of Hillel's L3 homework.\033[0m"
      "\n\n\033[0;30;47m All rights reserved :)\033[0m")
operation = ""
while operation != "q":
    operation = input("\nEnter arithmetic operation you're going to calculate ('+', '-', '*' or '/')"
                      "\nOtherwise, type 'q' to quit: ")
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        first_number = float(input("\nPLEASE ENTER FIRST NUMBER: "))
        second_number = float(input("PLEASE ENTER SECOND NUMBER: "))
        if operation == "+":
            result1 = first_number + second_number
            print("\n\033[1;32;40mYour result: \033[0m" + str(result1))
        elif operation == "-":
            result2 = first_number - second_number
            print("\n\033[1;32;40mYour result: \033[0m" + str(result2))
        elif operation == "*":
            result3 = first_number * second_number
            print("\n\033[1;32;40mYour result: \033[0m" + str(result3))
        else:
            result4 = first_number / second_number
            print("\n\033[1;32;40mYour result: \033[0m" + str(result4))
    elif operation == "q":
        print("\n\033[0;30;47m Thanks for using TestCalc. <3 Hugs and kisses <3\033[0m")
    else:
        print("\n\033[1;31;40m ¯\_(ツ)_/¯ Sorry, currently TestCalc supports only 4 operations mentioned above.\033[0m")
