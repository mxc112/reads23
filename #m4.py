#m4 

#ex00
#!/usr/bin/env python3

def main():
    # Prompt the user to enter a word
    word = input("Enter a word: ")
    
    # Display the word in uppercase
    print(word.upper())

if __name__ == "__main__":
    main()

#ex01
#!/usr/bin/env python3
def main():
    age = int(input("Please enter your age: "))
    print(f"Your current age is {age}.")
    print(f"In 10 years, you will be {age + 10}.")
    print(f"In 20 years, you will be {age + 20}.")
    print(f"In 30 years, you will be {age + 30}.")
if __name__ == "__main__":
    main()

#ex02
#!/usr/bin/env python3

def main():
    print("--- Simple Calculator ---")
    
    try:
        # Prompt user and store numbers as numeric values (floats)
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    # Perform calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Display results
    print("\n--- Results ---")
    print(f"Addition ({num1} + {num2})         = {addition}")
    print(f"Subtraction ({num1} - {num2})      = {subtraction}")
    print(f"Multiplication ({num1} * {num2})   = {multiplication}")

    # Handle potential division by zero
    if num2 != 0:
        division = num1 / num2
        print(f"Division ({num1} / {num2})         = {division}")
    else:
        print(f"Division ({num1} / {num2})         = Undefined (cannot divide by zero)")

if __name__ == "__main__":
    main()

#ex03
#!/usr/bin/env python3

def main():
    # Prompt the user to enter a number
    user_input = input("Enter a number: ")
    
    try:
        # Convert the input to a float to evaluate it mathematically
        number = float(user_input)
        
        # Check if the number has a fractional part (is a decimal)
        # We check both the string input (for explicit '.' like 3.0) and modulo (for 3.5)
        if '.' in user_input or number % 1 != 0:
            print(f"The number {user_input} is a decimal.")
        else:
            print(f"The number {user_input} is not a decimal (it's a whole number/integer).")
            
    except ValueError:
        print("Error: Please enter a valid numeric value.")

if __name__ == "__main__":
    main()

#ex04
#!/usr/bin/env python3

import math

def main():
    try:
        # Prompt the user to enter a number
        user_input = input("Enter a number: ")
        
        # Convert the input to a float so it can handle decimals
        number = float(user_input)
        
        # Round the number up using math.ceil()
        rounded_number = math.ceil(number)
        
        # Display the result
        print(f"The number {number} rounded up is: {rounded_number}")
        
    except ValueError:
        print("Error: Please enter a valid numeric value.")

if __name__ == "__main__":
    main()

#ex05
#!/usr/bin/env python3

def main():
    # Prompt the user to enter a string
    user_string = input("Enter a string: ")
    
    # Swap the case (uppercase to lowercase, and lowercase to uppercase)
    swapped_string = user_string.swapcase()
    
    # Display the result
    print(swapped_string)

if __name__ == "__main__":
    main()

