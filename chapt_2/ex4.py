# A customer in a store is purchasing five items. Write a program that asks for the price of each item,
# then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

item1 = float(input("What is the price of the first item? $"))

item2 = float(input("What is the price of the second item? $"))

item3 = float(input("What is the price of the third item? $"))

item4 = float(input("What is the price of the fourth item? $"))

item5 = float(input("What is the price of the fifth item? $"))

tax = 0.07
subtotal = item1 + item2 + item3 + item4 + item5
total = (tax * subtotal) + subtotal

# The "format" method converts subtotal to a string and displays it as only 2 decimal places
print('The subtotal of the sale is $', format(subtotal, '.2f'))
print('The amount of sales tax is 7%')
print('The total comes to $', format(total, '.2f'))
