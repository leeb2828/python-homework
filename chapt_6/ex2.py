# Write a program that asks the user for the name of a file.
# The program should display only the first five lines of the
# file's contents. 
                 
# If the file contains less than five lines, it should
# display the file's entire contents.

def main():
    # Get the name of the file from the user
    filename = input('Enter the name of a file (include the extension): ')
    
    # Open the file
    file_obj = open(filename, 'r')

    while True:
        line = file_obj.readline()
        line = line.rstrip('\n')
        if (line == ''):
            break
        else:
            print(line)
    
    # Close the file
    file_obj.close()

main()

