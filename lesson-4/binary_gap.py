# Find the maximal sequence of consecutive zeros that surrounded by ones
# at both ends in the binary representation of a number entered by User.
# Examples:
# 9 as a binary number is 1001. The Binary gap is equal to 2 (there are two consecutive zeros in this number).
# 529 as a binary number is 1000010001. The Binary gap is equal to 4.
number = int(input('Enter a valid number: '))
def to_bin(number):
    bin_num = ''
    while number > 0:
        bin_num += str(number % 2)
        number //= 2 # only grabs the divisible part
    return bin_num[::-1]

print(to_bin(number))

def binary_gap(bin_number):
    max_gap = 0
    counter = 0
    for i in str(bin_number):
        if i == '0':
            counter += 1
        elif i == '1':
            if counter > 0 and counter > max_gap:
                max_gap = counter
            counter = 0
    return max_gap

print(binary_gap(to_bin(number)))

