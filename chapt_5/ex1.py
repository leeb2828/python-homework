# Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles. 
# The conversion formula is as follows: Miles = Kilometers X 0.6214

def convert_to_miles(kilo):
    miles = kilo * 0.6214
    miles = int(miles)

    return miles

def main():
    # Get the distance in kilometers from the user
    distance_in_kilo = int(input("Enter the distance in kilometers: "))
    distance_in_miles = convert_to_miles(distance_in_kilo)

    print('That distance in miles is', distance_in_miles)


# call main function
main()
