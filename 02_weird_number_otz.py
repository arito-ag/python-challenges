"""
    Context: A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
    Challenge: Given an integer, n, perform the following conditional actions:
        - If n is odd, print Weird
        - If n is even and in the inclusive range of 2 to 5, print Not Weird
        - If n is even and in the inclusive range of 6 to 20, print Weird
        - If n is even and greater than 20, print Not Weird
        
    Input Format:
    A single line containing a positive integer n

    Constraints:
    1 <= n <= 100

    Output Format:
    Print Weird if the number is weird. Otherwise, print Not Weird.

    Sample Input:
    3

    Sample Output:
    Weird
"""

def print_n_type():
    n = int(input("Enter the number: ").strip())
    if 1 <= n <= 100:
        if n % 2 != 0 or (n % 2 == 0 and 6 <= n <= 20):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Number is lower than 1 or greater than 100")

if __name__ == "__main__":
    print_n_type()