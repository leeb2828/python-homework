# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
#
# Write a program that calculates the average of all the numbers stored in the file.

def main():
    total = 0
    num_of_items = 0

    file_obj = open('numbers.txt', 'r')
    for line in file_obj:
        num = int(line)
        total += num
        num_of_items += 1

    print("The average of the numbers is", (total // num_of_items))

main()