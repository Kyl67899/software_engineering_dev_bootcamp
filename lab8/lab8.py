"""
 Long line of comments
 April 20th, intro python
"""

#single lins comment
print(f"------- Example 1: print ------- ")
print("Hello World") #print hello world
print(f"------- Example 2: data type ------- ")
print(f"Data type of 3.56: {type(3.56)}")
print(f"Data type of -25: {type(-25)}")
print(f"Data type of 'Hello world': {type('Hello world')}")
print(f"Data type of '$': {type('$')}")
print(f"Data type of false: {type(False)}")

print(f"------- Example 3: variables ------- ")
#declare variables
num1 = 25.5
num2 = -22
user_name = "joe scam"
add_num = num1 + num2
print(f"{user_name} has {add_num} ")

print(f"------- Example 4: multiple variables ------- ")
score1=score2=score3=55

print(f"score1: {score1}, score2: {score2}, score3: {score3}")

print(f"------- Example 5: input command ------- ")
i = input("Enter your name")
print(f"Collected username = {i}")

# print("Enter your luck #")
luckyNum = int(input("Enter your luck #"))
print(f"Lucky num = {luckyNum}")

#double luck num
dbluckyNum = luckyNum * 2
print(f"Doubled Lucky num = {dbluckyNum}")

# cast int num or float into string
triplenum = str(luckyNum) * 3
print(f"tripled the cast num = {triplenum}")

# cast int num to boolean value
completed_task = -3
print("completed task = ", bool(completed_task))

print(f"------- Example 6: arithmetic operators ------- ")
num=2
num1=45

print(f"The sum of {num} and {num1} is {num+num1}")
print(f"The difference of {num} and {num1} is {num1-num}")
print(f"The product of {num} and {num1} is {num*num1}")
print(f"The division of {num} and {num1} is {num1/num}")
print(f"The floor division of {num} and {num1} is {num1//num}")
print(f"The modulus of {num} and {num1} is {num1%num}")
print(f"The exponent of {num} and {num1} is {num**num1}")

print(f"------- Example 7: finding hypotenuse ------- ")
# declare and assign variables
x = float(input("Enter side 1:"))
y = float(input("Enter side 2:"))

print(f"------- Example 8: assigning operators ------- ")
n = 6
print(f"number = {n}")

#assignment operators +
n+=3
print(f"number + 3 = {n}")

# assignment operator -
n-=4
print(f"updated - number = {n}")

# assignment operator * 
n*=2
print(f"updated * number = {n}")

# assignment operator /
n/=3
print(f"updated / number = {n}")

# assignment operator //
n//=15
print(f"updated // number = {n}")

# assignment operator **
n**=10
print(f"updated ** number = {n}")

# assignment operator % or remainder
n%=5
print(f"updated %= number = {n}")

print("------- Example 9: comparison operators ------- ")
n1 = 10
n2 = 20
n3 = 1

compare1 = n1 == n2
compare2 = n1 ==(n2-n3)

print(f"n1 == n2: {compare1}")
print(f"n1 == (n2-n3): {compare2}")

compare3= n1 != n2
compare4= n1 != (n2-n3)

print(f"n1 != n2: {compare3}")
print(f"n1 != (n2-n3): {compare4}")

print("------- Example 10: string indexing ------- ")
username = "peterpan123"
# positive index
print(f"the fifth character in {username} is {username[4]}")

# negative index
print(f"the last character in {username} is {username[-3]}")

print("------- Example 11: string slice ------- ")

# string slice
# slice from the beginning to the 4th character
print(f"The first 4 characters in {username} is {username[:4]}")

# slice from the 5th character to the end
print(f"Slice from the 6th characters in {username} is {username[5:]}")

# slcie from 3rd to 7th character
print(f"Slice from the 3rd to 7th characters in {username} is {username[2:7]}")

# slcie from -3rd to -6th character
print(f"Slice from the 3rd to 7th characters in {username} is {username[-3:-6]}")

print("------- Example 12: total characters in string (len) ------- ")

# string length
print(f"Total characters = {len(username)} characters")

print("------- Example 13: total characters in string (len) ------- ")
username = "pan124"
print(f"The username = {username}. End of username")
username.strip()
print(f"The username after method strip = {username}. End of username")

print("------- Example 14: total characters in string (len) ------- ")
username = username.lower()
print(f"The username after method strip = {username}. End of username")
username = username.upper()
print(f"The username after method strip = {username}. End of username")

print("------- Example 15:  ------- ")
username = username.replace('P', "%")
print(f"The username after replace method = {username}. End of username")

print("------- Example 16:  ------- ")
msg = "Introduction to Python Programming! Today we are learning string methods"
print(f"Message = {msg}")
print(f"Message after split method = {msg.split('!')}")

print("------- Example 17: find the method ------- ")
# find the letter 'P'
# index_P = msg.find('P')



print("------- Example 18:  ------- ")

#check if the word 'we' is in the msg string

answer_msg = 'we' in msg

print(f"is the word 'we' in the msg string? = {answer_msg}")

answer_today = "Today" not in msg

print(f"is the word 'today' NOT in the 'msg' string? = {answer_today}")

print("------- Example 19: list indexing  ------- ")

color = ["orange", "magenta", "olive"]

numbers = [6, 20, -5, 4, 45]

mixedList = ["per", False, 56, True, "test"]

emptyList = []

print(f"colors list = {color}")
print(f"numbers list = {numbers}")
print(f"empty list = {emptyList}")

print(f"2nd color = {color[1]}")
print(f"1st number = {numbers[0]}")

print(f"last color = {color[-1]}")
print(f"3rd last number = {numbers[-3]}")

print("------- Example 20: + * operator on list ------- ")

#concatenate the first last color
new_color = color[0] + color[-1]
print(f"The new color is = {new_color}")

# concatenate the 2nd color with the 3rd number
# new_word = color[1] + numbers[2] # --> type error
# print(f"The new word is = {new_word}")

print("------- Example 21: remove items in list ------- ")
# remove the last color
color.pop(-1)
print(f"colors after pop = {color}")

print("------- Example 22: remove items in list ------- ")
# add items to the end of the list colors
color.append("PINK")
print(f'colors after append = {color}')

# add the new item to a list 
color.append(["blue", "green"])
print(f"colors after the append = {color}")

# add multiple items to a list 
# color.append("RED", "PURPLE") # --> argument error
print(f"colors after append = {color}")

print("------- Example 23: sort a list ------- ")
colors = ['orange', 'magenta', 'olive', 'magenta']

print(f"color list =", colors)

colors.sort()

print(f"color list sorted ", colors)

bool_list = [True, False, True]
bool_list.sort()
print(f"bool list sorted = {bool_list}")

print("------- Example 24: count method ------- ")
count_true = bool_list.count(True)
print(f"There is {count_true} True values")
count_red = colors.count("red")
print(f"There is/are {count_red} red colors")

print("------- Example 25: length of a list ------- ")
length_color = len(colors)
print(f"There is/are {length_color} color")

print("------- Example 26: idex of a item in a list ------- ")
#index of color "olive"
index_olive = colors.index("olive")
print(f"The index of color olive is {index_olive}")

# index_green = colors.index("green") # --> value error
# print(f"The index of color green is {index_green}")

