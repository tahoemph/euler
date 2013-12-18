largest = (0, None, None)
for mult1 in range(999, 99, -1):
    for mult2 in range(mult1 - 1, 99, -1):
        number = mult1*mult2
        if mult1*mult2 > largest[0]:
            number_str = str(number)
            if number_str == number_str[::-1]:
                largest = (mult1*mult2, mult1, mult2)
print largest
