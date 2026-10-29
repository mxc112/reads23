#m7
#ex00
#!/usr/bin/env python3

import sys

def main():
    # Check if the number of parameters passed is different from 1 (excluding script name)
    if len(sys.argv) != 2:
        print("none")
        return
        
    target_word = sys.argv[1]
    
    # Prompt the user to enter a word (using an empty input prompt to ensure 
    # clean stdout for automated testing/grading environments)
    user_input = input()
    
    # Compare the user input with the parameter
    if user_input == target_word:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()



#ex01
#!/usr/bin/env python3

import sys

def main():
    # Get parameters (excluding the script name itself)
    args = sys.argv[1:]
    
    # Check if no parameters are provided
    if not args:
        print("none")
    else:
        # Display the total number of parameters
        print(f"parameters: {len(args)}")
        
        # Display each parameter and its length
        for arg in args:
            print(f"{arg}: {len(arg)}")

if __name__ == "__main__":
    main()


#ex02
#!/usr/bin/env python3

import sys

def main():
    # Check if the number of parameters passed is different from 1 (excluding script name)
    if len(sys.argv) != 2:
        print("none")
        return
        
    text = sys.argv[1]
    
    # Count the number of 'z' characters in the string
    z_count = text.count('z')
    
    # If there are no 'z' characters, display "none"
    if z_count == 0:
        print("none")
    else:
        # Display "z" for each occurrence, joined together
        print("z" * z_count)

if __name__ == "__main__":
    main()


#ex03
#!/usr/bin/env python3

import sys

def main():
    args = sys.argv[1:]
    
    # If there are no parameters, display "none"
    if not args:
        print("none")
        return
        
    # Iterate over each parameter
    for arg in args:
        # Skip parameters that already end with "ism"
        if arg.endswith("ism"):
            continue
        
        # Display the parameter with "ism" appended
        print(arg + "ism")

if __name__ == "__main__":
    main()

#ex04
#!/usr/bin/env python3

import sys

def main():
    # Check if the number of parameters passed is different from 2 (excluding script name)
    if len(sys.argv) != 3:
        print("none")
        return
        
    try:
        # Convert parameters to integers
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("none")
        return
        
    # The first number must be strictly smaller than the second one
    if start >= end:
        print("none")
        return
        
    # Construct a list containing all the values between the two numbers (inclusive)
    result_list = list(range(start, end + 1))
    
    # Display the array using the print function
    print(result_list)

if __name__ == "__main__":
    main()