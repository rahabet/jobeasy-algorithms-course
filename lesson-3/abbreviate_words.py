# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris = > S.H

def abbrev_name(name):
    abbrev = ''
    if len(name.split(' ')) > 2:
        print('You are only allowed to enter two words')
    else :
        first_letter = name[0].capitalize()
        second_letter_index = name.find(' ') + 1
        second_letter = name[second_letter_index].capitalize()
        abbrev = f'{first_letter}.{second_letter}'
    return abbrev
print(abbrev_name('hello world'))