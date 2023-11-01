import array

#array str
var = array.array('u', "tdtdtrty")
print(var)
print(len(var))

#signed int
num = array.array('i', [2, 3, 5, 6])
print(num)
print(type(num))

#Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Julius', 26)

print(p1.name)
print(p1.age)
print(p1)

#Another class
class Pupil:
    def __init__(weight, name, company):
        weight.name = name
        weight.company = company
    
    def show(weight):
        print(f"I'm + {weight.name} I work at {weight.company} ")

p2 = Pupil("Glory Olasanmi", "LevelUp")
Pupil.show(p2)
