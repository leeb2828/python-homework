# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The
# formula is as follows:
# F = 9/5C + 32
# The program should ask the user to enter a temperature in Celsius, then display the
# temperature converted to Fahrenheit.

celsius_temp = int(input('Enter the temperature in Celsius: '))
fahrenheit_temp = ((9/5) * celsius_temp) + 32
print('Temperature in Fahrenheit is ' + str(fahrenheit_temp) + ' degrees.')
