# Calculating the Factorial of a Number (without using Recursion)
# In mathematics, the notation n! represents the factorial of the nonnegative 
# integer n. The factorial of n is the product of all the nonnegative integers
# from 1 to n. For example,
#       7! = 1 X 2 X 3 X 4 X 5 X 6 X 7 = 5,040
# and
#       4! = 1 X 2 X 3 X 4 = 24
# Write a program that lets the user enter a nonnegative integer then uses a loop
# to calculate the factorial of that number. Display the factorial.

factorial = int(input("Enter a non-negative integer: "))
loop_control = factorial

while loop_control > 1:
    print(factorial, 'X', (loop_control - 1))
    factorial = factorial * (loop_control - 1)
    loop_control -= 1

print('The factorial for that number is', factorial)


