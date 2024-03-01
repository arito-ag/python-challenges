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
    range_two_and_five = range(2,5)
    range_six_and_twenty = range(6,20)
    n = int(input("Enter the number: ").strip())
    if 1 <= n <= 100:
        if n % 2 != 0:
            print("Weird")
        elif n % 2 == 0:
            if n in range_two_and_five:
                print("Not Weird")
            elif n in range_six_and_twenty:
                print("Weird")
            elif n >= 20:
                print("Not Weird")
    else:
        print("Number is lower than 1 or greather than 100")

if __name__ == "__main__":
    print_n_type()