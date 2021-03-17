# When given a list of elements find the two lowest elements. They can be equal to each
# other or different.
import sys

def print2Smallest(arr):
    arr_size = len(arr)
    if arr_size < 2:
        print("Invalid Input")
        return
    first = second = sys.maxsize

    for i in range(0, arr_size):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif (arr[i] < second and arr[i] != first):
            second = arr[i]

    if (second == sys.maxsize):
        print("No second smallest element")
    else:
        print(f'The smallest element is {first}, and second smallest element is, {second}')

print2Smallest([5,7,45,8,10,11,5,1])