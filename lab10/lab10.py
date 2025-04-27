"""
    Kyle Parsotan
    April 25 2025
"""

print("--- example 3: for loop with different increment")
#for loop to print from 2 to 30 with increment of 3
for num in range(2, 30, 3):
    print(num)
    
print("\n ---- example 4: for loop with different decrement---")
# for loop to print from 10 to 0, with a decrement of 2
for num in range (10,0, -2):
    print(num)
    
print("\n ------- example 5: for loop through a string --------")
username = "yes123"
for eachCharacter in username:
    print (eachCharacter)

print("\n -_----- example 6: nested conditional statement: count ---")
# for loop to check how many negative numbers are in the list
numbers = 15, -2, 0, 8, 9, -11
negCounter = 0

# prompt result
# print(f"The sum of all odd numbers is {sumodd}")

print("--- example 8: break statment in a loop")

# for loop to print from 0 to 10 () 
for n in range(0, 10):
    if n==5:
        print("counter reaches to")
        break
    else:
        print(n)
        
print("--- example 9: continue statement in a loop")
# for loop to add number from 0 to 10 exculsive except 5
sumall = 0
for n in range(10):
    if n == 5:
        print("skipping 5")
        continue
    sumall += n
    print(n)
    print(f"sum = {sumall}")
    
print("--- example 10: continue statement in a loop")
for n in range(6):
    if (n == 3):
        break
    print(n)
else:
    print("completed loop")

print("--- example 11: continue statement in a loop")
# while loop to collect and add numbers between -5 and 5 
# if the user enters a number that is not between -5 and 5, the while will terminate
sumusernumber = 0
while(True):
    num = int(input("Enter a number between -5 and 5: "))
    if number < -5 or number > 5:
        # if not (5>= number >= -5)
        break
    sumusernumber += number

#prompt result
print(f"The total sum is = {sumusernumber} ")


print("--- example 12: continue statement in a loop")


print("--- example 13: continue statement in a loop")
# while loop to count the even numbers in the list
num = [2, 0, -5, 1, 8, -6, 7, 4, 3]
index = 0
len_numbers = len(num)
evencount = 0

while index < len_numbers:
    if num[index]%2 == 0 and num[index]!=0:
        evencount += 1
    index += 1
else:
    print("There is/are {evencount} even numbers")

