# Zeros not for Heros
# Numbers ending with zeros are boring. They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

number = int(input('Please enter a number: '))

def discard_zeros(num):
    if num == 0:
        return 'invalid input'
    numero = str(num)
    last = numero[-1]

    if last == '0':
        heros = numero[:-1]
        return int(heros)
    else:
        return int(numero)

print(discard_zeros(number))
