# Prime Numbers
# A prime number is a number that is only evenly divisible by itself and 1.
# The number 5 is prime because it can be evenly divided by (only) 1 and 5.
# The number 6 however, is not prime because it can be divided evenly by
# 1, 2, 3, and 6.
# Write a boolean function named is_prime which takes an integer as an
# argument and returns true if the argument is a prime number, or false
# otherwise. Use the function in a program that prompts the user to enter
# a number then displays a message indicating whether the number is prime.

def is_prime(num):
    # if a number = 2 it is prime
    if num == 2:
        return True
    # prime number is ALWAYS greater than one
    # prime number is divisible (evenly) by 1 and itself
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    # if the number < 1 OR equal to one, it is NOT prime
    else:
        return False


def main():
    print("I will tell you if a number is prime or not prime")
    user_input = int(input("Enter a number: "))
    prime = is_prime(user_input)
    if prime:
        print("That is a prime number")
    else:
        print("That is NOT a prime number")


main()
