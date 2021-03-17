# When given a string the the code checks if there are repetitive characters and deletes all
# repetitions, leaving the first number in place followed by the number of repetitions.
#
# For Example: “aaaabbbccde” is changed to “a4b3c2de”

string_1 = input('Enter a string: ')

def string_compress(string):
    counter = 1
    result = string[0]
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            counter += 1
        else:
            if counter > 1:
                result += str(counter)
                counter = 1
            result += string[index + 1]
    else:
        if counter > 1:
            result += str(counter)
    return result

print(string_compress(string_1))
