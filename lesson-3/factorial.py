# When User enters a number, its factorial is displayed.

def num_factor(number):
    # return math.factorial(number)
    if number <= 0:
        print("Only positive integers for now")
    else:
        num = 1
        for n in range(num, number+1):
            num *= n
        return num

print(num_factor(3))