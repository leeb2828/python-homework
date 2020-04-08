# Write a program that asks the user for a number in the range of 1 through 7. The program
# should display the corresponding day of the week, where: 
# 1 = Monday
# 2 = Tuesday
# 3 = Wednesday 
# 4 = Thursday
# 5 = Friday
# 6 = Saturday
# 7 = Sunday
# The program should display an error message if the user enters a number that is outside the range of 1 through 7.

user_number = int(input("Enter a number in the range of 1 through 7: "))

if user_number == 1:
    print("Today is Monday")
elif user_number == 2:
    print("Today is Tuesday")
elif user_number == 3:
    print("Today is Wednesday")
elif user_number == 4:
    print("Today is Thursday")
elif user_number == 5:
    print("Today is Friday")
elif user_number == 6:
    print("Today is Saturday")
elif user_number == 7:
    print("Today is Sunday")
else:
    print("Error: You must enter a number in the range of 1-7")

    