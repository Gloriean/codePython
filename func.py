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


def total_calc(bill_amount, tip_perc=10):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

def volume_of_cuboid(length, breadth, height):
    return length*breadth*height
volume_of_cuboid(5, 6, 8)

def add(num1, num2):
    print("The sum of two nos: ")
    num3 = num1 +  num2

add(num1=8,num2=3)

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

#Python Lambda
