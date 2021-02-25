# Check if given number is a prime number
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

# You have a given number. Find all prime numbers before the given number

number = int(input('Enter a number: '))

def prime_number(num):
    prime = []
    if number <= 0:
        return "Number must be greater than 0"
    for n in range(1, num+1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            prime.append(n)
    return prime

print(prime_number(number))

