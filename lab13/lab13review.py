"""
Kyle Parsotan
May 5th, 2025
"""

# exmple of init
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return {f"Username = {user1.name} \n User age = {user1.age}"}
        
    def __str__(self):
        return {f"Hello, I am {self.name}"}
        

# example 2
class Chair:
    # accessible
    chair_color = "yellow"
    
    def __init__(self, height, width, length):
        self.__width = width
        self.length = length
        self.chairheight = height
        
    def __str__(self):
        return {f"Username = {user1.name} \n User age = {user1.age}"}
        
    def __str__(self):
        return {f"Hello, I am {self.name}"}
      
    # method to pass the length
    def pass_length(self):
        return self.length
    
    # method to return the volume of the chair
    def chair_volumne(self):
        return self.__width * self.length * self.chairheight
    
    def get_color(self):
        return self.chair_color
    
    def chair_description(self):
        return f"The total volume of the chair is {self.chair_volumne()} cubic units The chair colorr is {self.chair_color}"
    
    def selfprice(self, price):
        self._charPrice = price
        
        
# create a object of the class
userChair = Chair(30, 4, 65)
user1 = Person("kyle", 20)
print(f"Username = {user1.name} \n User age = {user1.age}")
print(f"The chair width = {user1.name} \n User age = {user1.age}")
print(f"Username = {user1.name} \n User age = {user1.age}")
print(userChair.chair_description())

#chair price
userChair.selfprice(200)
print(f"The price od the chair is {userChair._charPrice}")