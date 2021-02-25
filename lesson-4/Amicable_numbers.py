# Check if two numbers are friendly to each other or not.
#
# Friendly number:
# n1 sum of divisors (except an n1) are equal to n2 and sum of divisors n2 are equal to n1.
# For example: 220 and 284
# 220: divisors [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
# 284: divisors [1, 2, 4, 71, 142]

def amicable_numbers():
    num_1 = int(input("Enter an integer: "))
    print(f'The divisors of {num_1} are: ', end='')
    div_num1 = []
    sum_num1 = 0
    sum_num2 = 0
    for i in range(1, num_1):
        if num_1 % i == 0:
            div_num1.append(i)
    print(div_num1)
    for num in div_num1:
        sum_num1 += num
    print(f'The sum of the divisors is: {sum_num1}\n')

    num_2 = int(input("Enter an integer: "))
    print(f'The divisors of {num_2} are: ', end='')
    div_num2 = []
    for i in range(1, num_2):
        if num_2 % i == 0:
            div_num2.append(i)
    print(div_num2)
    for nu in div_num2:
        sum_num2 += nu
    print(f'The sum of the divisors is: {sum_num2}\n')

    if sum_num1 == num_2 and sum_num2 == num_1:
        print(f'{num_1} and {num_2} are friendly numbers')
    else:
        print(f'{num_1} and {num_2} are not friendly numbers')

amicable_numbers()
