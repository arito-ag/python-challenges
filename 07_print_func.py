"""
    Challenge: 
        Without using any string methods, try to print the following:
        123...n
        Note that "..." represents the consecutive values in between.
    
    Input Format:
    - The first line contains an integer n.

    Output Format:
    - Print the list of integers from 1 through n as a string, without spaces.

    Sample Input:
    3

    Sample Output:
    123

    Constraints:
    1 <= n <= 150
"""


def print_sequence_as_string(n):
    numbers_string = ""
    for i in range(1, n+1):
        numbers_string += f"{i}"
    print(numbers_string)


if __name__ == "__main__":
    n = int(input())
    if not 1 <= n <= 150:
        print("n must be between 1 and 150 range")
    else:
        print_sequence_as_string(n)
