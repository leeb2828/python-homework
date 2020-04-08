def changing_list(list1):
    # initialize another empty list
    list2 = []
    for index in range(len(list1)):
        # Get rid of newline characters
        current_item = list1[index].rstrip('\n')
        # split up current index item into another array
        item = current_item.split()
        for i in range(len(item)):
            list2.append(int(item[i]))

    return list2

def main():
    # initialize total and average
    total = 0
    average = 0
    # Create the file object
    file_obj = open('numbers_same_line.txt', 'r')

    # initialize empty list
    list1 = []

    for line in file_obj:
        list1.append(line)
    
    list2 = changing_list(list1)
    for i in range(len(list2)):
        total += list2[i]

    print("The total is", total, "and the average is", (total // (len(list2))) )


# Call main method
main()




         


    

