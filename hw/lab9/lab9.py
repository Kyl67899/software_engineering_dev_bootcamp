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

# def calculate_gpa(grade1, grade2):
#     average = (grade1 + grade2) / 2
#     if 90 <= average <= 100:
#         gpa = "A"
#     elif 70 <= average <= 89.99:
#         gpa = "B"
#     elif 60 <= average <= 69.99:
#         gpa = "C"
#     elif 0 <= average <= 59.99:
#         gpa = "FAIL!"
#     else:
#         gpa = "UNDEFINED!"
#     return average, gpa

# grade1 = float(input("Enter the first grade: "))
# grade2 = float(input("Enter the second grade: "))

# # Calculate the average and GPA using the function
# average, gpa = calculate_gpa(grade1, grade2)

# # Print the result
# print(f"For the average of {average}, your GPA is {gpa}.")

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

