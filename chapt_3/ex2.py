# The area of a rectangle is the rectangle's length times its width. 
# Write a program that asks for the length and width of two rectangles. 
# The program should tell the user which rectangle has the greater area, or
# if the areas are the same.

first_len = int(input("What is the length of the first rectangle? "))
first_width = int(input("What is the width of the first rectangle? "))
area1 = first_len * first_width

print()

second_len = int(input("What is the length of the second rectangle? "))
second_width = int(input("What is the width of the second rectangle? "))
area2 = second_len * second_width

if area1 > area2:
    print("Rectangle #1 has the greater area")
elif area2 > area1:
    print("Rectangle #2 has the greater area")
else:
    print("Both rectangles have the same area")

