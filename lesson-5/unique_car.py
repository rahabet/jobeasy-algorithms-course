# When given a string the code deletes all duplicates leaving only one of each character.
# For example:
# “asdasdasdqwewqsazx” should convert to “asdqwezx”

string = input('Enter a string: ')

def unique_char_string(string):
    #option-1
    # result = ''
    # for char in string:
    #     if result.count(char) == 0:
    #         result += char
    # return result

    # option-2
    result = ''
    for char in string:
        if char not in result:
            result += char
    return result

    #option-3
    # return ''.join(set(string))





print(unique_char_string(string))
