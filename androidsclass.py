def digit_sum(number):
    size = len(number)
    list_digits = number.split("")
    if (size ):
    else:
        for i in range (size):
            sum = list_digits[i] + digit_sum(list_digits[i+1])
        return sum






for i in range (4):
    number1 = input()
    size = len(number)
    digit_sum(size, number)
