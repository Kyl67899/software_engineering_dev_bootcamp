"""

Create a Python code that will calculate an average of two grades and return a GPA according to the average.
The program should: 
Collect two grades from the keyword. Collect the two numbers as 'float' values.
Use the two grades to find the average of them using the formula --> average = (grade1+grade2)/2. 
Use the average grade in a flow mechanism (conditional statement) to display the GPA according to the calculated average as: 
Average 90 and 100, GPA = A
Average 89.99 and 70, GPA = B 
Average 69.99 and 60, GPA = C 
Average 59.99 and 0, GPA = FAIL! 
Any other average = UNDEFINED! 

The program should print the result at the end as: 

For the average of ____, your GPA is _____.

"""

grade1 = float(input("Enter your first grade"))
grade2 = float(input("Enter your second grade"))
avgGPA = (grade1+grade2/2)

# function grades(grade1, grade2){}

match avgGPA:
    case avgGPA if 90 >= avgGPA <= 100:
        gpa = "GPA A"
    case avgGPA if 89.99 <= avgGPA >= 70:
        gpa = "GPA B"
    case avgGPA if 69.99 <= avgGPA >= 60:
        gpa = "GPA C"
    case avgGPA if 59.99 <= avgGPA >= 0:
        gpa = "GPA = FAIL"
    case _:
        gpa = "GPA = FAIL"
        
print(f"For the average of {avgGPA}, your GPA is {gpa}")
