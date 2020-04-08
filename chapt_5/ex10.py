# One foot equals 12 inches. Write a function named feet_to_inches that accepts a number of feet as an 
# argument and returns the number of inches in that many feet. Use the function in a program that prompts the user 
# to enter a number of feet then displays the number of inches in that many feet.

def feet_to_inches(user_num):
    inches = user_num * 12
    return inches

def main():
    # Get number from user
    user_input = int(input("Enter number of feet: "))
    num_of_inches = feet_to_inches(user_input)

    print("The number of inches in that many feet is", num_of_inches)


# Call main method
main()
    