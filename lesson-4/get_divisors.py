# a number (less than a given number) that divides into a given number with out a remainder.
# (remainder of division with them must be equal to zero)


number = int(input("Enter an integer number: "))

def get_divisor(num):
    divisors = []
    index = 1
    while index <= num:
        if num % index == 0:
            divisors.append(index)
        index += 1
    return divisors

print(get_divisor(number))