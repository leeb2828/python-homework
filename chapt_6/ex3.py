# Write a program that asks the user for the name of a file.

# The program should display the contents of the file with each line 
# preceded with a line number followed by a colon. The
# line numbering should start at 1.

def main():
    # loop control for the while-loop
    num = 1
    # Ask user for the name of the file
    user_input = input("Enter the name of the file (extension included): ")

    # Create the file object and assign it to variable "f"
    f = open(user_input, 'r')
    
    # Read the file's contents
    while(True):
        line = f.readline()
        line = line.rstrip('\n')
        # if it's the end of the file
        if (line == ''):
            break
        else:
            print(num, ":", line)
            num += 1

    # Close the file
    f.close()

# Call the main function
main()