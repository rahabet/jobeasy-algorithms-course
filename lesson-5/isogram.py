# Isogram is a word with no repeating letters, in a row or not.
# Create a Python function to check is word isogram. Empty string - isogram. Case doesn’t matter.

string = input('Enter a string: ')
def is_isogram(string):
    uniq = ''.join(list(set(string)))
    return len(uniq) == len(string)


print(is_isogram(string))
