"""
Kyle Parsotan
April 27, 2025
"""

#import math module
import math 

print("---- Example 3: function that doesnt return values")
# ex 3
def greeting():
    print("Welcome to functions!")
    
# ex 4
print("---- Example 4: function with parameter")
def printusername(username):
    print(f"Welcome to the function {username}")
    

print("---- Example 4: function with parameter")
def printusername(username):
    print(f"Welcome to the function {username}")

print("---- Example 4: function with parameter")
def printusername(username):
    print(f"Welcome to the function {username}")

print("---- Example 5: function with default parameter")
def user_country(username="_", country="unknown country"):
    print(f"{username} is living in {country}")
    return

# example 6
def product(n1=1, n2="unknown"):
    return n1 * n2

#ex 7 
def multiple(n):
    if n%3 == 0 and n!=0:
        return True
    else:
        return False
    
# example 8 composition function
# define function to collect, validate, and return a number between 1
def collectnum():
    n = float(input("Enter a number between 1 and 9 (inclusive)"))
    # validate the number
    while(not(1 <= n <= 9)):
        n = float(input("Re-enter a number again: "))
    return n
    
def sumnumbers(totalnumbers = 0):
    sum = 0
    for n in range(totalnumbers):
        sum += collectnum()
    return sum
    
# function to print value
def printresult(totalsum):
    print(f"Sum of all numbers is = {totalsum}")
    
# example 9 
# define a function to calculate and return the area of the circle

#formula = r^2 * pi
def areaCircle(radius):
    a = math.pow(radius, 2) * math.pi
    return round(a, 2)

# function to print result
def areaprint(area, r=0):
    print(f"The area of the circle with {r} radius is {area}")

# function to return the ratio of two numbers (hours)
def ratioHours(hour):
    try:
        dayhour = 24
        rad = dayhour/hour 
    except ZeroDivisionError: 
        print("Zero error")
        print("There was an error in the division")
    except ValueError:
        print("Value error")
        print("There was an error in the division")
        return 0
    except:
        print("general exception")
    else:
        print("division is fine")
        return rad
    finally:
        print("--- process completed ---")

# example 11
# defining a class name 'myClass'
class Myclass:
    # property (attribute)
    id = 12345
    
    #method
    def facetime(self):
        return "Welcome to class"
    
# example 12
class Complexnumber():
    # instatiate of the class
    def __init__(self, realnumber, imgnumber):
        self.r = realnumber
        self.r = imgnumber
        
# example 13
class Car:
    # instatiate of the class
    def __init__(self, make, model, year):
        self.carmake = make
        self.carmodel = model
        self.caryear = year
        
    # set properly 'odometer'
    odometer_reading = 0
    
    # method to return descriptive of the car
    def get_car_description(self):
        return f"{self.carmake} with model {self.carmodel} was made on {self.caryear}"
    
    # method to read the odometer
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"
    
    # method to update the odometer
    def update_odometer(self, milage):
        if milage > self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("Odometer cant\t roll back")
            
    # method to add miles into the calculator
    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Can\t add negative miles")
