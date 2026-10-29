# reads23

#m2
#commands
chmod +x xx.py
./ xx.py

#ex00 iszero
#!/usr/bin/env python3

number = float(input("Enter a number: "))

if number == 0:
    print("This number is equal to zero.")
else:
    print("This number is different from zero.")

#ex01 isneg

#!/usr/bin/env python3

number = float(input("Enter a number: "))

if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")

#ex02 password
#!/usr/bin/env python3

password = "Python is awesome."

if password == "Python is awesome.":
        print("ACCESS GRANTED")
else:
        print("ACCESS DENIED")

#ex03 mult
#!/usr/bin/env python3

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = number1 * number2

if result < 0:
  print("The result is negative.")
elif result > 0:
  print("The result is positive.")
else:
  print("The result is both positive and negative.")

#m3
#ex00 to25
#!/usr/bin/env python3

number=int(input("Enter a number: "))

if number > 25:
        print("Error")
else:
        for i in range(number, 25):
                number = number + 1
                print(f"Inside the loop, my variable is {number}")

#ex01 multiplication
#!/usr/bin/env python3


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

#m5
#ex00
#!/usr/bin/env python3

def main():
    # Define a list of numbers
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    # Display the list
    print("The defined list of numbers is:")
    print(numbers)

if __name__ == "__main__":
    main()

#ex01
#!/usr/bin/env python3

def main():
    # Define the original list of numbers
    original_list = [5, 10, 15, 20, 25]
    
    # Iterate over the original list to create a new list where 2 is added to each value
    modified_list = []
    for number in original_list:
        modified_list.append(number + 2)
        
    # Display both lists on the screen
    print("Original list:", original_list)
    print("Modified list:", modified_list)

if __name__ == "__main__":
    main()

#ex02
#!/usr/bin/env python3

def main():
    # Define the original list of numbers (including values <= 5 and > 5)
    original_list = [3, 5, 6, 8, 10]
    
    # Iterate over the original list, processing only values greater than 5
    modified_list = []
    for number in original_list:
        if number > 5:
            modified_list.append(number + 2)
            
    # Display both lists on the screen
    print("Original list:", original_list)
    print("Modified list:", modified_list)

if __name__ == "__main__":
    main()

#ex03
#!/usr/bin/env python3

def main():
    # Define the original list of numbers (including duplicates, values <= 5, and > 5)
    original_list = [3, 5, 6, 6, 8, 10, 10]
    
    # Iterate over the original list, processing only values greater than 5
    modified_list = []
    for number in original_list:
        if number > 5:
            modified_list.append(number + 2)
            
    # Use a set to remove duplicates specifically in the output
    unique_output = set(modified_list)
    
    # Display both lists on the screen
    print("Original list:", original_list)
    print("Modified list (with duplicates removed in output):", unique_output)

if __name__ == "__main__":
    main()

#ex04
#!/usr/bin/env python3

import sys

def main():
    # Calculate the number of parameters passed (excluding the script name itself)
    num_params = len(sys.argv) - 1
    
    # Display the number followed by a newline
    print(num_params)

if __name__ == "__main__":
    main()


    







