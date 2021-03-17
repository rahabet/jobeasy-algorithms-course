# User enters a string using a keyboard. Write a Python function to check if it is palindrome
# or not. A string is said to be a palindrome if a reversed string is the same as the string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.

# Example:
# radar == radar
# radix != xidar

string = input("Enter a string: ")

def palindrome_check(word):
    return word == word[::-1]

print(palindrome_check(string))
