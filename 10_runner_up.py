"""
    Challenge: 
        Given the participants' score sheet for your University Sports Day, 
        you are required to find the runner-up score. 
        You are given n scores. Store them in a list and find the score of the runner-up.

    Input Format:
        The first line contains n. 
        The second line contains an array A[] of n integers each separated by a space.
    
    Output Format:
        Print the runner-up score.

    Sample Input:
    5
    2 3 6 6 5

    Sample Output:
    5

    Constraints:
    2 <= n <= 10
    -100 <= A[] <= 100
"""


def get_runner_up(n, scores=[]):
    # Remove high_score
    scores.remove(max(scores))
    # Return new best score
    return max(scores)


if __name__ == "__main__":
    n = int(input())
    # Remove duplicate scores and generate list
    scores = list(set([int(score) for score in input().split()]))
    print(get_runner_up(n, scores))
