"""
    Context: 	
        In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

    Challenge: 
        You are given a polynomial P of a single indeterminate (or variable), x.
        You are also given the values of x and k. Your task is to verify if P(x) = k.

    Input Format:
        The first line contains the space separated values of x and k.
        The second line contains the polynomial P.
    
    Output Format:
    Print True if P(x) = k. Otherwise, print False.

    Sample Input:
    1 4
    x**3 + x**2 + x + 1

    Sample Output:
    True

    Constraints:
    All coefficients of polynomial P are integers.
    x and k are also integers.
"""


def evaluate_polynomial(values, polynomial=""):
    x, k = values
    polynomial = polynomial.replace("x", x)
    result = eval(polynomial)
    return result == int(k)


if __name__ == "__main__":
    values = input().split()
    if not (all(value.isdigit() for value in values) and len(values)) == 2:
        print("x and k must be integer numbers and only enter two numbers")
    else:
        polynomial = input()
        print(evaluate_polynomial(values, polynomial))
