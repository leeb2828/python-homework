# Write a program that asks the user to enter a number of seconds and works as follows:
    #   - There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60,
    #     the program should convert the number of seconds to minutes and seconds.

    #   - There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600,
    #     the program should convert the number of seconds to hours, minutes, and seconds.

    #   - There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400,
    #     the program should convert the number of seconds to days, minutes, and seconds.


user_input = int(input('Enter number of seconds: '))

# Convert number of seconds --> days, minutes, and seconds
if user_input >= 86400:
    days = user_input // 86400
    # Take the "leftover" seconds and plug it back into user_input 
    user_input = user_input % 86400 

    minutes = user_input // 60
    user_input = user_input % 60

    seconds = user_input 
    
    print('DAYS:', str(days))
    print('MINUTES:', str(minutes))
    print('SECONDS:', str(seconds))
    
# Convert number of seconds --> hours, minutes, and seconds.
elif user_input >= 3600:
    hours = user_input // 3600
    user_input = user_input % 3600

    minutes = user_input // 60
    user_input = user_input % 60
    seconds = user_input 

    print('HOURS:', str(hours))
    print('MINUTES:', str(minutes))
    print('SECONDS:', str(seconds))

# Convert number of seconds --> minutes and seconds
elif user_input >= 60:
    minutes = user_input // 60
    user_input = user_input % 60
    seconds = user_input 

    print('MINUTES:', str(minutes))
    print('SECONDS:', str(seconds))

# Print seconds
else:
    print('SECONDS:', str(user_input))
