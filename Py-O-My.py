print("\033[0;30;47m This TestCalc is made by Max Lekontsev in scope of Hillel's L3 homework.\033[0m")
print("\n\n\033[0;30;47m All rights reserved :)\033[0m")
operation = ''
while operation != "q":
    operation = input("\nEnter arithmetic operation you're going to calculate ('+', '-', '*' or '/')"
                      "\nOtherwise, type 'q' to quit: ")
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        first_number = ''
        second_number = ''
        first_no_error = ''
        second_no_error = ''
        result = 0
        while not first_no_error:
            try:
                first_number = float(input("\nPLEASE ENTER FIRST NUMBER: "))
                first_no_error = True
            except ValueError:
                print("\n\033[1;31;40m :( Only numbers allowed!\033[0m")
                first_no_error = False
        while second_no_error is not True or (operation == "/" and second_number == 0):
            try:
                second_number = float(input("\nPLEASE ENTER SECOND NUMBER: "))
                if operation == "/" and second_number == 0:
                    print("\n\033[1;31;40m ^_^ You can't divide by 0!\033[0m")
                else:
                    pass
                second_no_error = True
            except ValueError:
                print("\n\033[1;31;40m :( Only numbers allowed!\033[0m")
                second_no_error = False
        # print("All good")
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        else:
            result = first_number / second_number
        print("\n\033[1;32;40m Your result: \033[0m" + str(result))
    elif operation == "q":
        print("\n\033[0;30;47m Thanks for using TestCalc. <3 Hugs and kisses <3\033[0m")
    elif operation == "'+'" or operation == "'-'" or operation == "'*'" or operation == "'/'" or operation == "'q'":
        print("\n\033[1;31;40m ;) Try without quotes.\033[0m")
    else:
        print("\n\033[1;31;40m ¯\_(ツ)_/¯ Sorry, currently TestCalc supports only 4 operations mentioned above.\033[0m")
