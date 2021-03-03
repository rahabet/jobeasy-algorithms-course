# A Narcissistic Number is a positive number which is the sum of its own digits,
# each raised to the power of the number of digits in a given base. In this Kata,
# we will restrict ourselves to decimal (base 10).
#
# For example, take 153 (3 digits), which is narcisstic:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# The Challenge:
# Your code must return true or false depending upon whether the given number is a Narcissistic number
# in base 10. Error checking for text strings or other invalid inputs is not required, only valid
# positive non-zero integers will be passed into the function.

number = input("Enter a positive number: ")

def narcissistic(num):
    sum = 0
    length = len(num)
    for n in num:
        sum = sum + int(n) ** length
        number = int(num)

    if (number == sum):
        return "true"
    else:
        return "false"
print(narcissistic(number))

