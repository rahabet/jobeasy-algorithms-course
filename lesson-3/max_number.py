# Find max number from 3 values, entered manually from a keyboard

num1 = int(input('Enter number: '))
num2 = int(input('Enter number: '))
num3 = int(input('Enter number: '))

print(f'the max of {num1}, {num2}, {num3} is: ')

def max_number(n1,n2,n3):
    max =0

    if n1 > n2 and n1 > n3:
        max = n1
    elif n2 > n1 and n2 > n3:
        max = n2
    else:
        max = n3

    return max

print(max_number(num1,num2,num3))