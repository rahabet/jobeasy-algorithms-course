# Find divisor of two or more integers, which are not all zero, is the largest positive integer
# that divides each of the integers.
# Example:

# What is the greatest common divisor of 54 and 24?
# The number 54 can be expressed as a product of two integers in several different ways:
# 54 * 1 = 27 * 2 = 18 * 3 = 9 * 6. Thus the divisors of 54 are: 1, 2, 3, 6, 9, 18, 27, 54.
# Similarly, the divisors of 24 are: 1, 2, 3, 4, 6, 8, 12, 24.
# The numbers that these two lists share in common are the common divisors of 54 and 24:
# 1,2,3,6.
# The greatest of these is 6. That is, the greatest common divisor of 54 and 24 is 6.

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

def euclidean(num1, num2):

    if num1 > num2:
        num = num1 % num2
        if num2 % num == 0:
            print(f'the greatest common divisor between {num1} amd {num2} is: {num}')
    else:
        num = num2 % num1
        if num1 % num == 0:
            print(f'the greatest common divisor between {num1} amd {num2} is: {num}')

euclidean(num1, num2)
