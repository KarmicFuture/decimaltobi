#convert decimal number into binary

decimal_number = 432
binary_list = []
while (int(decimal_number) >> 0):
    mod = decimal_number % 2
    decimal_number = decimal_number// 2
    print(decimal_number, "    ", mod)
    binary_list.append(mod)

print(binary_list[::-1])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
