    # """
    # April 24, conditional statement
    # """
    
print(f"---- example 1: if statement")

age = 20

agecode = 123

if age >= 21:
    print("You are an Adult!")
    agecode = 200
    
print(f"After the 'if' statement, agecode = {agecode}")

print(f"---- example 2: if statement")
if age >= 21:
    print("You are adult!")
    agecode = 200
else:
    print("You are under 21!")
    agecode = 100

print(f"---- example 3: if statement")

age = 50
if 0 <= age < 21:
    print("You are a minor")
elif 21 <= age < 65:
    print("You are an adult")
elif 65 <= age <= 130:
    print("You are a senior citizen")
else:
    print("unable to read age!")
    

print(f"---- example 4: if statement ----")

temp = 90
humidity = 50

if 70 <= temp <= 90 and humidity < 80:
    print("The wesather is pleasant")
else: 
    print("The weather is not ideal")
    
print(f"---- example 5: or operator")

day = "monday"
is_holiday = True

if day=='Saturday' or day=="Sunday" or is_holiday:
    print("you can relax today")
else:
    print("It is a workday")
    
    
print(f"---- example 6: if statement ----")
num = int(input("Enter a number:"))
if (num >= 0):
    if num == 0:
        print("The number is zero")
    else:
        print(f"{num} is positive")
        
else:
    print(f"{num} is negative")
    
print(f"---- example 7: nested condition ----")
# username validation username 3+ characters
username = input("Enter a username").strip()
len_username = len(username)

if len_username >= 3:
    index_whitespace = username.find(" ")
    if index_whitespace == -1:
        print(f"{username} is valid")
    else:
        print(f"{username} is CAN NOT have whitespace")
else:
    print(f"{username} is invalid. username must have 3+ characters.")
    
    
print(f"---- example 8: match-case condition ----")
res_code = 404

match res_code: 
    case 400:
        print(f"Code = {res_code}. Server CANNOT understand")
    case 401 | 403:
        print(f"Code = {res_code}. Server refused to send back")
    case 404:
         print(f"Code = {res_code}. Server CANNOT understand")
    case _:
        print("INVALID CODE")


