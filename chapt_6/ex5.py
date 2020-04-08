# Assume a file containing a series of integers is named numbers.txt
# and exists on the computer's disk.

# Write a program that reads all of the numbers stored in the file and 
# calculates their total

# Note: If you come up with your own numbers.txt file, keep individual numbers on separate lines in 
# the text file

def other_way():
    total = 0
    # "with" statement usage
    with open('numbers.txt', 'r') as file:
      for line in file:
          total += int(line)

      # Notice that I didn't have to write file.close()
      # Link: https://www.pythonforbeginners.com/files/with-statement-in-python 
    print('The total of the numbers is', total)


def main():
    total = 0
    
    # Create file object
    file_obj = open('numbers.txt', 'r')

    for line in file_obj:
        total += int(line)

    print('The total of the numbers is', total)

    # Close the values
    file_obj.close()



# Call main function
main()
# Call other function
other_way()


    

