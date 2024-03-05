"""
    Context: The provided code stub reads two integers from STDIN, a and b. 
    Challenge: The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2.
    
    Input Format:
    - The first and only line contains the integer, n.

    Output Format:
    Print n lines, one corresponding to each i.

    Sample Input:
    5

    Sample Output:
    0
    1
    4
    9
    16

    Constraints
    1 <= n <= 20
"""


def print_square_numbers(n):
    for i in range(0, n):
        print(i**2)


if __name__ == "__main__":
    n = int(input())
    if not 1 <= n <= 20:
        print("n must be between range 1 to 20")
    else:
        print_square_numbers(n)
