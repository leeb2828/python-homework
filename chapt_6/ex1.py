# Assume a file containing a series of integers is named numbers.txt and
# exists on the computer's disk. Write a program that displays all of the
# numbers in the file.

def main():
    # In order for this program to work with a saved file, this program must
    # create a file object in memory.
    
    # Open the file and assign to a variable
    infile = open('numbers.txt', 'r')

    # Read the file's contents
    contents = infile.read()

    # Close the file
    infile.close()

    # Print the contents to the terminal
    print(contents)


# Call the main function
main()

# Notes:
# Once a program is finished with a file, it should close the file.
# In some systems, failure to close an output file can cause a loss
# of data. This happens because the data that is written to a file is 
# is first written to a buffer, which is a small "holding section" in memory.
# When the buffer is full, the system writes its' contents to the file.
# The process of closing an output file forces unsaved data that remains in 
# the buffer to be written to the file.