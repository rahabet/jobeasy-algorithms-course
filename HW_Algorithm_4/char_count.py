# Write a Python function, which will count how many times a character (substring) is included in
# a string. DON’T USE METHOD COUNT

sentence = input("Enter sentence: ").lower()
word = input("Enter the word to search: ").lower()

def substring(stat):
    occurence = 0
    sent = stat.split()
    for i in sent:
        if i == word:
            occurence += 1
    return occurence

print(f'The word {word} has occured {substring(sentence)} times')



