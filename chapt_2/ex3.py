# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
# enter the total square feet in a tract of land and calculates the number of acres in the tract.

# Hint: Divide the amount entered by 43,560 to get the number of acres.

one_acre_to_square_feet = 43560
total_square_feet = int(input("Enter the total amount of square feet: "))

number_of_acres = total_square_feet / one_acre_to_square_feet
number_of_acres = format(number_of_acres, '.2f')

print(number_of_acres, "acres.")




