# Learning outcome: Test the student's ability to use a for loop to find a specific item in an existing list.
# Activity description:
# complete class examples
# complete lab exercise
# Lab exercise description:
# Given the following list:
# colors = ['red', 'orange', 'olive', 'magenta', 'green']
# complete the code by writing a Python program that:
# Takes a color input from the user using the keyboard.
# Strips any leading/trailing whitespace from the input.
# Converts the input to lowercase.
# Uses a for loop and a nested conditional statement to check whether the entered color is in the list colors.
# Uses a flag to indicate when the color is found, and breaks the loop once a match is found.
# Prints a message depending on whether the color was found in the list.

# Note: Replace the blank with the entered color.

# colors = ['red', 'orange', 'olive', 'magenta', 'green']

# user_color = input("Enter your color: ").strip().lower()

# found = False

# for color in colors:
#     # If the color is found:
#     # {user_color} color is in the list
#     if user_color == color:
#         if found == True:
#             print(f"{user_color} color is in the list")
#             break
#         else:
#             print(f"{user_color} color IS NOT in the list")
#     # If the color is not found:
#     # {user_color} color IS NOT in the list
    



colorss = ['red', 'orange', 'olive', 'magenta', 'green']

user_colors = input("Enter your color: ").strip().lower()

found = False

for color in colorss:
    # If the color is found:
    # {user_color} color is in the list
    if user_colors == color:
        if found == False:
            colorss.append(user_colors)
            print(f"{user_colors} color was not in the list, so it has been added")
            break
        elif found == True:
            print("{user_colors} color was found in the list.")
    # If the color is not found:
    # {user_color} color IS NOT in the list
print(f"Updated colors list: ", colorss)