# Enter a string of words separated by spaces. Find the longest word.


sentence = input("Enter sentence: ")

# Finding longest word
longest = max(sentence.split(), key=len)

# Displaying longest word
print("Longest word is: ", longest)
print("And its length is: ", len(longest))
