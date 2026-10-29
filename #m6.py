#m6
#ex00
#!/usr/bin/env python3

import sys

def main():
    # Calculate the number of parameters passed (excluding the script name itself)
    num_params = len(sys.argv) - 1
    
    # Display the number followed by a newline
    print(num_params)

if __name__ == "__main__":
    main()


#ex01
#!/usr/bin/env python3

import sys

def main():
    # Check if exactly one parameter is passed (excluding the script name itself)
    if len(sys.argv) == 2:
        print(sys.argv[1].upper())
    else:
        print("none")

if __name__ == "__main__":
    main()

#ex02
#!/usr/bin/env python3

import sys

def main():
    # Check if exactly one parameter is passed (excluding the script name itself)
    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        print("none")

if __name__ == "__main__":
    main()

#ex03
#!/usr/bin/env python3

import sys

def main():
    # Check if there are fewer than two parameters (excluding the script name itself)
    if len(sys.argv) < 3:
        print("none")
    else:
        # Iterate over the parameters in reverse order and print each one
        for param in reversed(sys.argv[1:]):
            print(param)

if __name__ == "__main__":
    main()

#ex04
#!/usr/bin/env python3

import sys

def main():
    # Check if the number of parameters is different from 2 (excluding script name)
    if len(sys.argv) != 3:
        print("none")
        return
        
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # Count how many times the keyword appears in the text
    count = text.count(keyword)
    
    # If the keyword does not appear (count is 0), display "none"
    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()