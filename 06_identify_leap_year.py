"""
    Context: 	
        An extra day is added to the calendar almost every four years as February 29,
        and the day is called a leap day. 
        It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.
        A leap year contains a leap day.

        In the Gregorian calendar, three conditions are used to identify leap years:
        - The year can be evenly divided by 4, is a leap year, unless:
            - The year can be evenly divided by 100, it is NOT a leap year, unless:
                - The year is also evenly divisible by 400. Then it is a leap year.

        This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
        while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

    Challenge: 
        Given a year, determine whether it is a leap year. 
        If it is a leap year, return the Boolean True, otherwise return False.

    Input Format:
        Read year, the year to test.
    
    Output Format:
    The function must return a Boolean value (True/False).

    Sample Input:
    1990

    Sample Output:
    False

    Constraints:
    1900 <= year <= 10^5
"""


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_leap_v2(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    year = int(input())
    if not 1900 <= year <= 10 ** 5:
        print("The year must be between 1900 and 10^5 range")
    else:
        print(is_leap_v2(year))
