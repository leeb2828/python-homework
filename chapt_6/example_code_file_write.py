# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt
    outfile = open('philosophers.txt', 'w')

    # Write the names of three philosophers
    # to the file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # close the file
    outfile.close()

# call the main function
main()