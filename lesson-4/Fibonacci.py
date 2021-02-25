# Fibonacci sequence is starting from 0 or 1 and keeps adding the previous numbers
# 1,1,2,3,5,8,13,21,34...

# Display all the numbers from start to n of the fibonacci sequence.

number = int(input('Please enter a number: '))


def fibonacci_seq(n):
    if n < 0:
        return 'Invalid input, Enter integer number'
    if n == 0:
        return 0
    if n == 1:
        return 1
    index = 3
    fib_1 = 1
    fib_2 = 1

    while index < n:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        index += 1
    return fib_2

print(fibonacci_seq(number))



# def fibonacci_seq(n):
#     if n < 0:
#         return 'Invalid input, Enter integer number'
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return[1, 1]
#     index = 3
#     fib_1 = 1
#     fib_2 = 1
#     fib = [fib_1, fib_2]
#     while index <= n:
#         fib.append(fib_1 + fib_2)
#         fib_1, fib_2 = fib_2, fib_1 + fib_2
#         index += 1
#     return fib
#
#
# print(fibonacci_seq(number))