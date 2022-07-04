# 1. Write a Python program to print "Hello Python"?

print("Hello Python")

# 2. Write a Python program to do arithmetical operations addition and division.?

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition is ",a+b)
print("Division is ",a/b)

# 3. Write a Python program to find the area of a triangle?

b = int(input("Enter Breadth: "))
h = int(input("Enter Height: "))

print("Area of triangle is: ",0.5*b*h)

# 4. Write a Python program to swap two variables?

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Numbers before swapping are - ",a, ",",b)

temp = None

temp = a
a = b
b = temp

print("Numbers after swapping are - ",a, ",",b)

# 5.	Write a Python program to generate a random number?

import random as rd

print(int(rd.randint(1,1000)))