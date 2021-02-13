# When a user enters a year, the code detects if it is a leap year or not.
year = int(input('Input a year: '))
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f'{year} is not a leap year')

leap_year(year)