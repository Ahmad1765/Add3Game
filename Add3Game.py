import random
import time

# ANSI escape codes for color
RED = "\033[91m"
RESET = "\033[0m"

def generate_random_number():
    # Generate a 4-digit random number
    random_number = random.randint(1000, 9999)
    return random_number

def get_user_input():
    # Get user input for a number with digits increased by 3333
    user_input = int(input("Enter a 4-digit number with each digit increased by 3333: "))
    return user_input

def adjust_digit(value):
    # Adjust the digit, wrapping back to 0 if it reaches 9
    return (value + 3) % 10

def adjust_number(original_number):
    # Adjust each digit in the number
    adjusted_digits = [adjust_digit(int(digit)) for digit in str(original_number)]
    adjusted_number = int("".join(map(str, adjusted_digits)))
    return adjusted_number

def check_input(original_number, user_input):
    # Check if user input is correct
    adjusted_number = adjust_number(original_number)
    return adjusted_number == user_input

def main():
    while True:
        # Generate a random number
        random_number = generate_random_number()
        print(f"{RED}{random_number}{RESET}")
        
        # Get user input
        user_input = get_user_input()

        # Check if user input is correct
        result = check_input(random_number, user_input)

        # Display the result
        if result:
            print("Congratulations! Your input is correct.")
        else:
            print("Sorry, your input is not correct.")
            adjusted_number = adjust_number(random_number)
            print(f"The adjusted number is: {adjusted_number}")

        # Wait for 5 seconds
        time.sleep(1)

if __name__ == "__main__":
    main()
