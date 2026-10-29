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


    







