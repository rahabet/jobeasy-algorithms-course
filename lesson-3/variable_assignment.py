# User inputs two numbers. One number is assigned to a variable,
# the other number is assigned to b variable. The task is to invert the variables,
# so that the first variable contains the second number, while the first number is in the second variable.

def variable_assignment(a,b):
    a = int(input("Enter the first number a: "))
    b = int(input("Enter the second number b: "))
    # a,b = b,a  # simplest option that python allows us to do
    temp = a
    a = b
    b = temp
    print(f'a = {a} , b = {b}')

variable_assignment(5,10)

# another option
# a = a + b
# b = a - b
# a = a - b