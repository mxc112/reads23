# m2

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
