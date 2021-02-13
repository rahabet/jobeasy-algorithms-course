# Count odd and even numbers.  Count odd and even digits of the whole number.
# E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

number = int(input('Enter a valid number: '))
def count_parity(num):
    if num < 0 :
        print("Invalid number. Please enter a valid number")
    else :
        odd = 0
        even = 0
        str_num = str(num)
        for n in str_num:
            if int(n) % 2 == 0:
                even+= 1
            else:
                odd+= 1
        print(f'count even is: {even} \ncount odd is: {odd}')
         # return even, odd
count_parity(number)