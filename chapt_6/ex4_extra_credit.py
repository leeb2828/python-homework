def main():
    # Declare and initialize number of names
    name_count = 0
    
    # Open the file and create a file object
    the_file = open('extra_credit_names.txt', 'r')

    # Read the content of the file
    content = the_file.read()
    content = content.split(',')
    
    for name in content:
        # Trim whitespace from string with strip()
        print(name.strip())
        name_count += 1
    
    # Close the file
    the_file.close()

# Call the main function
main()
