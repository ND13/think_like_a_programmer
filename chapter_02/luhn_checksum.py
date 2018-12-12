# Luhn formula for validating identification numbers does not include producing check digit

number = "176248"
check_digit = 3
running_total = 0

numbers_list = [int(number[num]) for num in range(len(number))]

for i in range(len(numbers_list)):
    if i % 2 == 1:
        numbers_list[i] *= 2

    if numbers_list[i] >= 10:
        leftover = numbers_list[i] % 10
        numbers_list[i] = 1 + leftover
        
    running_total += numbers_list[i]

final_total = running_total + check_digit

print(final_total)
