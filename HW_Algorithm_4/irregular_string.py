# Enter an irregular string (that means it may have space at the beginning of a string, at the end
# of the string, and words may be separated by several spaces). Make the string regular
# (delete all spaces at the beginning and end of the string, leave one space separating words).

sentence = input("Enter sentence: ")

# print(sentence.split())
# split the sentence into lists then join them using whitespace

regular = " ".join(sentence.split())

# regular = sentence.strip().replace("  ", " ")

print(regular)

