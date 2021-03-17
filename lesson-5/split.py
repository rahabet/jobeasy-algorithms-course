# Given a string. Split it for two same parts. (if the string has odd characters,
# the first part should be greater by one character). Swap this parts and save the result in a
# new string and return it.

from math import ceil

string = input("Enter a word: ")

def split_in_half(string):
    string_len = len(string)
    half = ceil(string_len / 2)
    # half = string_len // 2
    print(half)
    left = string[:half]
    right = string[half:]
    print(left)
    print(right)
(split_in_half(string))