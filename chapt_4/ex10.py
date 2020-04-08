# Tuition Increase
# At one college, the tuition for a full-time student is $8,000 per semester.
# It has been announced that the tuition will increase by 3 percent each year
# for the next 5 years. Write a program with a loop that displays the projected
# semester tuition amount for the next 5 years.

tuition = 8000.00
tuition_increase = 0.03
new_tuition = 0

print(tuition)

for x in range(1, 6):
    tuition = (tuition_increase * tuition) + tuition
    new_tuition = round(tuition, 2)
    print(new_tuition)

