"""
Kyle Parsotan
Lab 11, class in Python (extra points)
"""

class Student:
    def __init__(self, name, age):
        # Initialize attributes here
        self.name = name #store name
        self.age = age # store age
        self.grades = {} # store grades
        
    def add_grade(self, subject, grades):
        self.grades[subject] = grades # store grades
        # Implement method to add grade
    def get_average_grade(self):
        if not self.grades:
            return 0 # zero division
        return sum(self.grades.values())/len(self.grades) # find the avg and / by len of values in the dict
            
        # Implement method to calculate average grade

# CALLING THE CLASS
# Create instances and demonstrate usage of each method
students = Student("Alice", 40)
students.add_grade("Math", 100)
students.add_grade("Computer Science", 80)

print(f"The average grade: {students.get_average_grade():.2f}")