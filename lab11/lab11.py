"""
   Kyle Parsotan
   April 27th, 2025    
"""

#import function
from lab11function import *
#import math module
import math 

print("---- Example 1: python dictionary ----")
# create a dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1984
}

# print the car dictionary
print(car)

# to access items in a dictionary we use [], where [] goes the key's name
print(f"The year of the car is ", car["year"])

# update the key value
car["year"] = 1980
print(f"The year of the car was updated to ", car["year"])

# add key:value pair
car["color"] = "red"
print(car)

print("--- Loop through dictionary ---")
for j in car:
    print(j)
    
for j in car:
    print(car[j])
    
for j in car:
    print(f"{j} has value = {car[j]}")
    
# given the following list create a dictionary that will counts the number of times that a word appears in the string. 
# create a dictionary to organize the words as the keys and the number of occupancy of the word as the value of the key

phase = "to be or not be"
print(f"original phrase = {phase}")
phase_split = phase.split()
print(f"splitted phase = {phase_split}")

# create the dictionary
word_count_dict = {}

#loop to each word in the list
for word in phase_split:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
        
print("Result of dictionary: ")
for w in word_count_dict:
    print(f"'{w}' = \t{word_count_dict[w]}")
    
print("---- Example 3: function that doesnt return values ---")

#run the functions
greeting()

print("---- Example 4: function with parameter ---")
printusername("peter user")
printusername("peter")

print("---- Example 5: function with default parameter")
user_country("kyle", "chile")
user_country("make sense", "argentina")

print("---- Example 6: function with return value ---")
# num1 = 2
# num2 = -6

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

prod1 = product(num1, num2)
print(f"The product of {num1} and {num2} is a {prod1}")
prod1 = product(num1)
print(f"The product is = {prod1}")
prod1 = product()
print(f"The product is = {prod1}")

print("---- Example 7: Boolean function ----")
checknum1 = multiple(num1)
checknum2 = multiple(num2)
print(f"Is {num1} multiple of 3? {checknum1}")
print(f"Is {num2} multiple of 3? {checknum2}")

print("---- Example 8: composition function ----")
# number = collectnum()
# print(number)
# test sumnumbers()
sumall = sumnumbers(4)
printresult(sumall)

print("---- Example 9: built in function ----")

r = 2
a = areaCircle(r)
areaprint(a, r)

print("---- Example 10: try-except ----")
ratio = ratioHours(0)
print(ratio)

try:
    ratio = ratioHours()
except:
    print("Error with the function")
    
print(ratio)

print("---- Example 10: try except ----")
r1 = ratioHours(0)
r2 = ratioHours(3)
r3 = ratioHours("peter")
# r4 = ratioHours(3)

print("---- Example 11: classes ----")
# create an instant of the class
id = Myclass()
print(f"An instance of the class = {id}")

# call the class property
user_id = id.id

print("---- Example 12: instantiation ----")
# create an instant of the class
paircomplexnumber = Complexnumber(2, 3)
# call the instance object 'r' of the class
real = paircomplexnumber.r
print(f"The real part is {real}")

print("---- Example 13: classes application ----")

# create an instantiate of the class
car1 = Car("Telsa", "S", 2023)
car_reading = car1.odometer_reading
print(f"Car miles reading = {car_reading}")

# call method get_car_description
print(car1.get_car_description())

# call method read_odometer
print(car1.read_odometer)

# update the odometer to milage = 10
car1.update_odometer(10)
print(car1.read_odometer())
car1.update_odometer(5)
print(car1.read_odometer())

# add 20 miles to the odometer
car1.increment_odometer(20)
print(car1.read_odometer())
car1.increment_odometer(-5)
print(car1.read_odometer())
car1.increment_odometer(8)
print(car1.read_odometer())