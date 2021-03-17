# When given a list, the program should return a list of all the elements that are below the
# arithmetical mean of the original list. The arithmetical mean is the sum of all elements
# divided by the number of elements.

import math
# list = list(input("Enter a list : "))

def arithmetic_mean(list):
    sum = 0
    global mean
    for a in list:
        sum += int(a)
    mean = sum / len(list)
    return mean

print(f'The mean is : {arithmetic_mean([19, 21, 46, 11, 18])}')

def list_of_elements(arr):
    val = len(arr)
    ar = []
    for i in range(0, val):
        if arr[i] < mean:
            ar.append(arr[i])
    return ar
print(f'The list of elements below the {mean} are {list_of_elements([19, 21, 46, 11, 18])}')

