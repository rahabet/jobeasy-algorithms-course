# Our code generates a random three-digit number and has to sum up all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16.

# --------------- Using random function-------------------

from random import randint


# random_number = randint(100, 999)
# print(f'random_number: {random_number}')
#
# def sum_of_three(number):
#
#     one_th = number % 10
#     number = number // 10
#     ten_th = number % 10
#     hundred_th = number // 10
#
#     return one_th + ten_th + hundred_th
#
# print(sum_of_three(random_number))

# ----------------------------------------

def sum_numbers(number):
    if number < 100 or number > 999:
        print("Wrong input! please enter numbers between 100 - 999")
    else:
        sum = 0
        for num in str(number):
            sum += int(num)
        print("The sum is:", end = ' ' )
        return sum

print(sum_numbers(157))