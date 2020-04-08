# Tip, Tax, and Total
#  - Write a program that calculates the total amount of a meal purchased at
#  - a restaurant. The program should ask the user to enter the charge for the
#  - food, then calculate the amounts of a 18% tip and a 7% sales tax.
#  - Display each of these amounts and the total.

meal_cost = float(input('Enter the total charge of the meal: '))
tip = round((0.18 * meal_cost), 2)
sales_tax = round((0.07 * meal_cost), 2)

print('Total cost of the meal: ' + str(meal_cost))
print('Tip amount: ' + str(tip))
print('Sales Tax: ' + str(sales_tax))
