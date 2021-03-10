# Find and replace a substring in a string for another substring. User enter from a keyboard a
# string and both substrings. DON’T USE METHOD REPLACE
import re

sentence = input("Enter sentence: ")
str_changed = input("Enter word to be changed: ")
str_change = input("Enter word to change with: ")


repl_sent = re.sub(str_changed, str_change, sentence, flags=re.IGNORECASE)

print(repl_sent)


