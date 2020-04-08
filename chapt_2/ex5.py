# Assuming there are no accidents or delays, the distance that a car travels down the interstate can be
# calculated with the following formula:
# Distance = Speed X Time

# A car is traveling at 70 miles per hour. Write a program that displays the following:
#      - The distance the car will travel in 6 hours.
#      - The distance the car will travel in 10 hours.
#      - The distance the car will travel in 15 hours.

speed = 70 # mph

time_6hours = 6 # hours
time_10hours = 10 # hours
time_15hours = 15 # hours

print("The car will travel", (speed * time_6hours), "miles in 6 hours.")
print("The car will travel", (speed * time_10hours), "miles in 10 hours.")
print("The car will travel", (speed * time_15hours), "miles in 15 hours.")

# EXTRA CREDIT
# Other ways to format the strings
print()

print('The car will travel {speed1} in six hours.'.format(speed1 = (speed * time_6hours)))
print('The car will travel ' + str(speed * time_10hours) + ' miles in ten hours.')
print('The car will travel ' + str(speed * time_15hours) + ' miles in fifteen hours.')
