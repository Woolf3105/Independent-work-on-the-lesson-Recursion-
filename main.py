def get_multiplied_digits(number):
    str_number = str(number)
    result = 1
    for digit in str_number:
        if digit != '0':
            result *= int(digit)
    return result


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)


