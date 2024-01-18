# Loop until the user enters a valid number
while True:
    # Get input from the user
    user_input = input("Enter a number: ")

    try:
        # Try to convert the input to an integer
        number = int(user_input)
    except ValueError:
        # If the input can't be converted to an integer, print an error message and continue the loop
        print("You didn't enter a valid number. Please try again.")
        continue

    # If the input was successfully converted to an integer, break the loop
    break

# Print the square of the number
print(f"Your number squared is {number**2}")