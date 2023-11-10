#Ej1
def is_even():
    if input == "even":
        return True
    else:
        return False
    



#Ej2

# Define a sample list
my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8]

# Use a for loop to iterate through the elements in the list
for element in my_list:
    # Check if the element is less than 5
    if element < 5:
        # Print the element if it satisfies the condition
        print(element)

#Ej3
import datetime

# Get user input for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculate the year when the user will turn 100
current_year = datetime.datetime.now().year
year_turn_100 = current_year + (100 - age)

# Print the message
print(f"Hello, {name}! You will turn 100 years old in the year {year_turn_100}.")



#Ej4
def merge_lists(list1, list2):
    # Use set to remove duplicates and then convert back to a list
    merged_list = list(set(list1 + list2))
    return merged_list

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = merge_lists(list1, list2)
print(result)


#EJ5
# Function to reverse a string using a loop
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        # Add each character to the beginning of the reversed string
        reversed_string = char + reversed_string
    return reversed_string

# Example usage
user_input = input("Enter a string: ")
result = reverse_string(user_input)
print("Reversed string:", result)


#Ej6
# Get user input for age
age = int(input("Enter your age: "))

# Check if the user is over 18 and provide an appropriate response
if age >= 18:
    print("You can come in.")
else:
    print("Sorry, you are not allowed in.")