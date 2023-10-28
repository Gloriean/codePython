def my_function():
    print("Hello! Hope you're doing well")
my_function()

def function(fname, lname):
    print(fname + " " + lname)

function("Glory", "Olasanmi")
function("Julius", "Idowu")
function("Favour", "Olasanmi")

def function1(fname, mname, lname):
    print(fname + " " + mname + " " + lname)

function1("Julius", "Oluwaropo", "Idowu")
function1("Sholape", "Opeyemi", "Ayinde")


#Calculate the bill_amount, tip_perc
def total_calc(bill_amount, tip_perc=10):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

#Volume of a Cuboid
def volume_of_cuboid(length, breadth, height):
    return length*breadth*height
print(volume_of_cuboid(5, 6, 8))

#Addition of two numbers
def add(num1, num2):
    print("The sum of two nos: ")
    num3 = num1 +  num2
    return (num1 + num2)

print(add(8, 3))
print(add(45, 12))

#Odd and even no
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(2)
evenOdd(3)   


def family(child1, child2, child3):
    print("It's difficult to recognize " + (child3))

family(child1 = "Bola", child2 = "Ayo", child3 = "Sola")

def list(food):
    food = ["maize", "rice", "beans", "yam", "noodles", "bread"]

lst = ['sugar', 'milk', 'cream', 'honey', 'butter podding']
list(lst)
print(lst)


#Python Lambda
str1 = 'GREEK'

lower = lambda string: string.lower()
print(lower(str1))

#Adding
x = lambda a : a + 10
print(x(5))

#Multiply
y = lambda b, c : b * c
print(y(5, 6))

#Function in Lambda
def myfunct(n):
    return lambda a : a * n

mydoubler = myfunct(2)
mytripler = myfunct(3)

print(mydoubler(11))
print(mytripler(11))