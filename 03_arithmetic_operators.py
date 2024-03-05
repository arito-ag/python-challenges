"""
    Context: The provided code stub reads two integers from STDIN, a and b. 
    Challenge: Add code to print three lines where:
    - The first line contains the sum of the two numbers.
    - The second line contains the difference of the two numbers (first - second).
    - The third line contains the product of the two numbers.
    
    Input Format:
    - The first line contains a number.
    - The second line contains b number.

    Output Format:
    Print the three lines as explained above.

    Sample Input:
    3
    5

    Sample Output:
    8
    -2
    15

    Constraints
    1 <= a <= 10^10
    1 <= b <= 10^10
"""


def get_operation_results(a=1, b=1):
    print(a + b)
    print(a - b)
    print(a * b)
    return


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    if not (1 <= a <= 10**10 and 1 <= b <= 10**10):
        print("Some of the numbers aren't in the range 1 to 10^10")
    else:
        get_operation_results(a, b)
