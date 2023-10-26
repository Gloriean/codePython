#A program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 2 for Monday and so on.
num = int(input("Enter any number from 1 - 7: "))

if num == 1:
    print("Sunday")
if num == 2:
    print("Monday")
if num == 3:
    print("Tuesday")
if num == 4:
    print("Wednesday")
if num == 5:
    print("Thursday")
if num == 6:
    print("Friday")
if num == 7:
    print("Saturday")
elif num > 7:
    print("It's invalid!")

#A program to accept a number from 1 to 12 and display name of the month and days in that month like for 1 for January and number of days 31 and so on. 
num1 = int(input("Enter a specific month: "))

if num1 == 1:
    print("January")
if num1 == 2:
    print("February")
if num1 == 3:
    print("March")
if num1 == 4:
    print("April")
if num1 == 5:
    print("June")
if num1 == 6:
    print("July")
if num1 == 7:
    print("August")

#exercise
name = "J"
print(len(name))

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50: 
    print("Name must be a maximum of 50 characters")
else: 
    print("Name looks good!")


#looping through a string
for x in "banana":
    print(x)

adj = ["red", "succulent", "juicy"]
fruits = ["watermelon", "orange", "pineapple"]

for x in adj:
    for y in fruits:
        print(x, y)

weather = 30
if weather < 30:
    print("I will mow the lawn")
    print("I will rest")
else:
    print("I won't mow the lawn")
