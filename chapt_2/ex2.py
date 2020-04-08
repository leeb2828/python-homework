# Sales Prediction
# A company has determined that its annual profit is typically 23% of total sales.
# Write a program that asks the user to enter the projected amount of total sales, then displays the
# profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

total_sales = float(input("Enter the projected amount of total sales: "))
profit = round((0.23 * total_sales), 2)
print('Your profit is ' + str(profit))
