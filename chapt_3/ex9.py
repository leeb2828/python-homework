# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
#    - Pocket 0 is green.
#    - For pockets 1 - 10, the odd-numbered pockets are red and the even-numbered
#       pockets are black.
#    - For pockets 11 - 18, the odd-numbered are black and the even-numbered are red.
#    - For pockets 19 - 28, the odd-numbered are red and the even-numbered are black.
#    - For pockets 29 - 36, the odd-numbered are black and the even-numbered are red.

# Write a program that asks the user to enter a pocket number and displays whether 
# the pocket is green, red, or black. The program should display an error message if 
# the user enters a number that is outside the range of 0 through 36.

# Get number from the user
user_choice = int(input('Enter a pocket number within the range of 0 - 36 : '))
pocket_color = ''

even_number = True
# Is the user number even or odd?
if user_choice % 2 == 0:
    even_number = True
else:
    even_number = False

if user_choice == 0:
    pocket_color = "green"
# For pockets 1 - 10
elif 0 < user_choice < 11:
    if (even_number):
        pocket_color = "black"
    else:
        pocket_color = "red"
# For pockets 11 - 18
elif 10 < user_choice < 19:
    if (even_number):
        pocket_color = "red"
    else:
        pocket_color = "black"
# For pockets 19 - 28
elif 18 < user_choice < 29:
    if (even_number):
        pocket_color = "black"
    else:
        pocket_color = "red"
# For pockets 29 - 36
elif 28 < user_choice < 37:
    if (even_number):
        pocket_color = "red"
    else:
        pocket_color = "black"
else:
    print('Error: You entered a number out of range')

print('The pocket color for that number is ' + pocket_color)