# Ask the user to input numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Convert the input string to a list of integers
number_list = list(map(int, user_input.split()))

print("Your list of numbers:", number_list)
