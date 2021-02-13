# Capitalize the first letter of words in a sentence

def cap_first_letter(string):
    word = string.split(' ')
    str = ""
    for i in word:
        if len(str) > 0:
            str = str + " " + i.strip().capitalize()
        else:
            str = i.capitalize()
    return str

print(cap_first_letter("How can mirrors be real if our eyes aren't real"))