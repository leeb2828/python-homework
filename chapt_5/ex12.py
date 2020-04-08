# Write a function named "max" that accepts two integer vaules as arguments and returns the value that 
# is the greater of the two. For example, if 7 and 12 are passed as arguments to the function, the function 
# should return 12. Use the function in a program that prompts the user to enter two integer values. 
# The Program should display the value that is the greater of the two.

def max(int1, int2):
    if (int1 > int2):
        return int1 
    elif (int2 > int1):
        return int2
    else:
        # They are both equal
        return int1


def main():
    # Get numbers from the user
    first_int = int(input("Enter the first integer: "))
    second_int = int(input("Enter the second integer: "))

    greatest_int = max(first_int, second_int)
    print("The greatest integer is", greatest_int, ".")


# Call main method
main()
