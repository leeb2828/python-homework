# On a roulette wheel, the pockets are numbered from 0 to 36.
# The colors of the pockets are as follows:
#   - Pocket 0 is green.
#   - For pockets 1 - 10, the odd-numbered pockets are red and the even-numbered
#     pockets are black.
#   - For pockets 11 - 18, the odd-numbered are black and the even-numbered are red.
#   - For pockets 19 - 28, the odd-numbered are red and the even-numbered are black.
#   - For pockets 29 - 36, the odd-numbered are black and the even-numbered are red.
# Write a program that asks the user to enter a pocket number and displays whether the
# pocket is green, red, or black. The program should display an error message if the user enters a
# number that is outside the range of 0 through 36.


def odd_or_even(opt):
    if opt % 2 == 0:
        return True
    else:
        return False


def get_pockets(choice):
    even = odd_or_even(choice)
    if choice == 0:
        return "green"
    # For pockets 1 - 10
    elif 0 < choice < 11:
        if even:
            return "black"
        else:
            return "red"
    # For pockets 11 - 18
    elif 10 < choice < 19:
        if even:
            return "red"
        else:
            return "black"
    # For pockets 19 - 28
    elif 18 < choice < 29:
        if even:
            return "black"
        else:
            return "red"
    # For pockets 29 - 36
    elif 28 < choice < 37:
        if even:
            return "red"
        else:
            return "black"
    else:
        print('You entered a number out of range. Please enter a number in range 0 - 36')
        new_input = int(input("Enter another number here : "))
        get_pockets(new_input)


user_choice = int(input('Enter a pocket number within the range of 0 - 36 : '))
pocket_color = get_pockets(user_choice)
print(pocket_color)

