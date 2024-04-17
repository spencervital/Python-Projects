# Function to calculate the area of a circle
def circle_area(diameter):
    radius = diameter / 2
    area = 3.14 * radius * radius
    return area


# Function that calculates the MPG
def mpg(distance, gallonsCount):
    mpgFunc = distance / gallonsCount
    return mpgFunc


# Function that calculates the total hours worked
def work_hours(work_hour_per_day):
    total_hours = sum(work_hour_per_day)
    return total_hours


# Function that calculates the average of three numbers
def average_numbers(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average


# Function that returns a name
def get_name(firstname, lastname):
    complete_name = firstname + " " + lastname
    return complete_name


print("Please select a mathematical calculation")
print("1. area of a circle")
print("2. MPG")
print("3. Total hours worked")
print("4. Average nof three numbers")
print("5. Name")
print("6. Invalid choice")

choice = int(input("Enter your choice: "))
if choice == 1:
    diameter = float(input("Enter diameter: "))
    area = circle_area(diameter)
    print("The area of the circle is: ", area)
elif choice == 2:
    distance = float(input("Please enter the distance: "))
    gallonsCount = float(input("Please enter the amount of gallons: "))
    mpgFunc = mpg(distance, gallonsCount)
    print("The MPG is: ", mpgFunc)

elif choice == 3:
    hours_worked_per_day = []
    for i in range(7):
        hours_worked = float(input("Enter the number of hours worked on day {}:".format(i+1)))
        hours_worked_per_day.append(hours_worked)
    total_hours = work_hours(hours_worked_per_day)
    print("You worked ", total_hours, " hours this week.")

elif choice == 4:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    average = average_numbers(num1, num2, num3)
    print("The average of the three numbers is: ", average)
elif choice == 5:
    fname = input("Enter a first name: ")
    lname = input("Enter a last name: ")
    name = get_name(fname, lname)
    print("the complate name is: ", name)
else:
    print("Invalid choice")
