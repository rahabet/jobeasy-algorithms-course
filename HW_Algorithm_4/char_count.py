# Write a Python function, which will count how many times a character (substring) is included in
# a string. DON’T USE METHOD COUNT

string = input("Enter a string: ").lower()
substring = input("Enter a substring: ").lower()

def occurence_of_substing (given_string, given_substring):
    counter = 0
    if len(given_string) < len(given_substring):
        return counter

    index = given_substring.find(given_substring)
    while index > -1:
        index = given_string.find(given_substring, index + 1)
        counter += 1
    return counter

# print(occurence_of_substing("hello world of hero's", "he"))

print(f'{substring}: is occured {occurence_of_substing(string, substring)} times')



