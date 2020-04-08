# Assume a file containing a series of names (as strings) is named names.txt and exists on the 
# computer's disk. Write a program that displays the number of names that are stored in the file.
# Hint: Open the file and read every string stored in it. Use a variable to keep a count of the number
# of items that are read from the file.

def main():
    # Declare and initialize number of names
    name_count = 0
    
    # Open the file and create a file object
    the_file = open('names.txt', 'r')
    
    for line in the_file:
        line = line.rstrip('\n')
        print(line)
    
    the_file.close()

# Call the main function
main()


