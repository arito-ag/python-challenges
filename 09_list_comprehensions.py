"""
    Context: 	
        List comprehensions are used to loop list with clean and eficient code lines

    Challenge: 
        You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
        Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j+ k is not equal to n. 

    Input Format:
        Four integers x, y, z and n, each on a separate line.
    
    Output Format:
        All permutations of [i, j, k]

    Sample Input:
    1
    1
    1
    2

    Sample Output:
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

    Constraints:
    0 <= i <= x
    0 <= j <= y
    0 <= l <= z
    Print the list in lexicographic increasing order.
"""


def get_permutations(x, y, z, n):
    return [[i, j, k] for i in range(
        x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(get_permutations(x, y, z, n))
