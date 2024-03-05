"""
    Context: 
        The provided code stub reads two integers, a and b, from STDIN. 
    Challenge: 
        Add logic to print two lines. The first line should contain the result of integer division, a // b. 
        The second line should contain the result of float division, a / b.
        No rounding or formatting is necessary.
    
    Input Format:
    - The first line contains a number.
    - The second line contains b number.

    Output Format:
    Print the two lines as explained above.

    Sample Input:
    3
    5

    Sample Output:
    0
    0.6
"""


def get_division_results(a=1, b=1):
    print(a // b)
    print(a / b)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    if (a == 0 or b == 0):
        print("Some of the numbers is equal to 0")
    else:
        get_division_results(a, b)
