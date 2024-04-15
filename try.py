# # def dice_sum_possibilities(dice_count, desired_sum):
# #     # table to store solutions to subproblems
# #     # table[i][j] will represent number of ways i dice can produce sum j
# #     table = [[0] * (desired_sum + 1) for _ in range(dice_count + 1)]

# #     # one way to produce sum 0 with 0 dice
# #     table[0][0] = 1

# #     # fill the table in bottom-up manner
# #     for i in range(1, dice_count + 1):
# #         for j in range(1, desired_sum + 1):
# #             for face in range(1, 7):
# #                 if j >= face:
# #                     table[i][j] += table[i - 1][j - face]

# #     return table[dice_count][desired_sum]

# # dice_count = 6
# # desired_sum = 22

# # possible_combinations = dice_sum_possibilities(dice_count, desired_sum)
# # total_outcomes = 6**6
# # probability = possible_combinations / total_outcomes

# # print(probability)

# def probability_of_picking_f_and_y(string):
#     count_f = string.count("f")
#     count_y = string.count("y")
    
#     # If either character doesn't exist, return 0 probability.
#     if count_f == 0 or count_y == 0:
#         return 0
    
#     total_characters = len(string)
    
#     # Calculate the probability of picking "f" first and "y" second
#     prob_f_first = (count_f / total_characters) * (count_y / (total_characters - 1))
    
#     # Calculate the probability of picking "y" first and "f" second
#     prob_y_first = (count_y / total_characters) * (count_f / (total_characters - 1))
    
#     # Return the total probability
#     return prob_f_first + prob_y_first

# string_input = "speedygonzalez1234"
# result = probability_of_picking_f_and_y(string_input)
# print(result)


# import pandas as pd

# # Create a list of data
# data = [
#     ["Laptop", "Electronics", 800.00, 50],
#     ["Smartphone", "Electronics", 400.00, 100],
#     ["T-shirt", "Apparel", 20.00, 500],
#     ["Headphones", "Electronics", 50.00, 200],
#     ["Backpack", "Accessories", 30.00, 150],
#     ["Jeans", "Apparel", 40.00, 300],
#     ["TV", "Electronics", 1000.00, 20],
#     ["Sunglasses", "Accessories", 15.00, 400],
#     ["Watch", "Accessories", 100.00, 80],
#     ["Sneakers", "Apparel", 60.00, 250],
# ]

# # Create a DataFrame
# df = pd.DataFrame(data, columns=["Product_Name", "Category", "Price", "Quantity_Sold"])

# # Calculate the total revenue for each category
# df_revenue = df.groupby('Category')['Price'].sum()

# # Find the category with the highest revenue
# highest_revenue_category = df_revenue.idxmax()

# # Get the total revenue for the highest revenue category
# highest_revenue = df_revenue.max()

# # Print the results
# print("The category with the highest revenue is:", highest_revenue_category)
# print("The total revenue for that category is:", highest_revenue)


# import pandas as pd

# # Create a list of data
# data = [
#     ["Laptop", "Electronics", 800.00, 50],
#     ["Smartphone", "Electronics", 400.00, 100],
#     ["T-shirt", "Apparel", 20.00, 500],
#     ["Headphones", "Electronics", 50.00, 200],
#     ["Backpack", "Accessories", 30.00, 150],
#     ["Jeans", "Apparel", 40.00, 300],
#     ["TV", "Electronics", 1000.00, 20],
#     ["Sunglasses", "Accessories", 15.00, 400],
#     ["Watch", "Accessories", 100.00, 80],
#     ["Sneakers", "Apparel", 60.00, 250],
# ]

# # Create a DataFrame
# df = pd.DataFrame(data, columns=["Product_Name", "Category", "Price", "Quantity_Sold"])

# # Calculate the total revenue for each category
# df_revenue = df.groupby('Category')['Price'].sum()

# # Find the category with the highest revenue
# highest_revenue_category = df_revenue.idxmax()

# # Get the total revenue for the highest revenue category
# highest_revenue = df_revenue.max()

# # Print the results
# print("The category with the highest revenue is:", highest_revenue_category)
# print("The total revenue for that category is:", highest_revenue)

import pandas as pd

# Create a list of data
data = [
    ["Wonder Cuzzi Resort", 100, 2580, 4.5],
    ["Royal Orbit", 45, 1200, 3.7],
    ["Sea Sights Resorts", 20, 2765, 4.8],
    ["Blue Moon Resort", 35, 453, 3.9],
    ["Ivory Bloom Resort", 200, 3125, 4.5],
    ["Happyland Resort", 150, 2089, 4.1],
    ["Haven Royale Resort", 75, 2109, 4.2],
    ["Sweet Dreams B&B", 80, 1267, 4.0],
    ["Resort On Main", 110, 1328, 3.4],
    ["Brownstone Resort", 100, 3258, 4.6],
    ["Double B On The Beach", 50, 850, 4.2],
]

# Create a DataFrame
df = pd.DataFrame(data, columns=["name", "room_price(USD)", "rate_count", "rate"])

# Filter the DataFrame to only include rows where the rate is higher than 4
df_filtered = df[df["rate"] > 4]

# Calculate the average price of rooms with a rate higher than 4
average_price = df_filtered["room_price(USD)"].mean()

# Print the average price
print(average_price)