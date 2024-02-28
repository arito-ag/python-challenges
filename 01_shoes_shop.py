"""
    Context: A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
    Challenge: Get the total sales amount per day given a list of shoe sizes and a shopping list
    Summary:  Raghus a shoe shop owner. His shop has X number of shoes.
    He has a list containing the size of each shoe he has in his shop.
    There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

    Your task is to compute how much money Raghu earned.

    Input Format:
    - The first line contains X, the number of shoes.
    - The second line contains the space separated list of all the shoe sizes in the shop.
    - The third line contains N, the number of customers.
    - The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

    Output Format:
    Print the amount of money earned by Raghu.

    Sample Input:
    10 - Number of shoes in the shop
    2 3 4 5 6 8 7 6 5 18 - Shoe sizes
    6 - Customers
    6 55 - Customer 1
    6 45 - Customer 2
    6 55 - Customer 3
    4 40 - Customer 4
    18 60 - Customer 5
    10 50 - Customer 6

    Sample Output:
    200
"""
shoe_amount = int(input("Shoe amount in the shop: ")) # X
size_list = []

shoe_sizes_input = input("Enter list of shoe sizes separated by space: ")
shoe_sizes_str = shoe_sizes_input.split()
shoe_sizes_int = [int(size) for size in shoe_sizes_str]

customers = int(input("Customers: ")) # N

amount = 0
for i in range(1,customers + 1):
    buy_input = input("Shoe size desired and price (separated by space): ")
    buy_str = buy_input.split()
    buy_int = [int(i) for i in buy_str]
    
    if buy_int[0] in shoe_sizes_int:
        shoe_sizes_int.remove(buy_int[0])
        amount += buy_int[1]
    else:
        continue

print(f"The amount of money earned by Raghu is: ${amount}")


