#m9
#ex00
#!/usr/bin/env python3

def array_of_names(namebook):
    # Build an array containing the full names with capitalized first letters
    full_names = []
    for first_name, last_name in namebook.items():
        # Capitalize both the first and last name components
        formatted_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(formatted_name)
    
    return full_names

def main():
    # Example dictionary associating first names with last names
    namebook = {
        "john": "doe",
        "jane": "smith",
        "alice": "wonderland"
    }
    
    # Call the method and display the resulting array
    result = array_of_names(namebook)
    print(result)

if __name__ == "__main__":
    main()