# User enters a string using a keyboard. Return result should be an inverted string.

string = input("Enter a word: ")

def reversed_string(string):
    # option-1
    # return string[::-1]
    # option-2
    return "".join(reversed(string))
    # option-3
    acc = ""
    index = len(string) - 1
    while index >= 0:
        acc += string[index]
        index -= 1
    return acc




print(reversed_string(string))
