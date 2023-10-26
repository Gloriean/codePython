a = 30
b = 200

if b > a:
    print("b is greater than a")
else:
    print("b is lesser than a")


#A program to check whether a number entered by user is even or odd.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("It's an Even number")
else:
    print("It's an Odd number!")

#A program to check whether a number is divisible by 7 or not.
num = int(input("Enter a number: "))

if number % 7 == 0:
    print("Divisible by 7!!")
else:
    print("Not divisible by 7!")

#A program to display "hello" if a number entered by user is a multiple of five, otherwise print "bye".
num1 = int(input("Enter a num: "))

if num1 % 5 == 0:
    print("Hello")
else:
    print("Bye")

#A program to check whether the last digit of a number (entered by user) is divisible by 3 or not.
num2 = int(input("Input your number: "))

if num2 % 3 == 0:
    print("It's divisible by 3")
else: 
    print("It's not divisible by 3")

#A program to accept % from the user and display the grade according to the ffg criteria:
grade = int(input("Enter your grade: "))

if grade > 90:
    print("You got an A!")
elif grade > 80 & grade <= 90:
    print("You got a B!")
elif grade >= 60 & grade <= 80:
    print("You got a C!")
else:
    print("You got a D!")
