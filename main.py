#convert decimal number into binary

def Dec_Num(decimal_number):
    while int(decimal_number) >> 0:
        mod = decimal_number % 2
        decimal_number = decimal_number // 2
        print(decimal_number, "    ", mod)
        binary_list.append(mod)


binary_list = []

number = input("What is the number you want to convert?   ")
decimal_number =int(number)

Dec_Num(decimal_number)

print(binary_list[::-1])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
