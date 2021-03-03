# Do the digital roots problem using recursion

num = int(input("Enter a number:"))

def digital_root(n):

    if(n < 10):
        return n
    n = n % 10 + digital_root(n//10)

    return digital_root(n)

print('\n' f'digital root of {num} is: {digital_root(num)}')
