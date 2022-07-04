# 1.	Write a Python program to convert kilometers to miles?

km = int(input("Enter kilometer : "))

print(("{a}km equals {b}miles".format(a=km, b=km/1.609344)))

# 2.	Write a Python program to convert Celsius to Fahrenheit?

#  F = (Celsius x 1.8) + 32

Celsius = int(input("Enter Celsius : "))

print(("{a}Celsius equals {b}Fahrenheit".format(a=Celsius, b=(Celsius*1.8)+32)))

# 3.	Write a Python program to display calendar?

import calendar

y = int(input("Enter a year : "))
m = int(input("Enter a month : "))

print(calendar.month(y, m))

# 4.	Write a Python program to solve quadratic equation?

import math

a = y = int(input("Enter value of a : "))
b = y = int(input("Enter value of b : "))
c = y = int(input("Enter value of c : "))

o1 = b*b-(4*a*c)
if o1<0:
    o1 = o1 + 2*o1

x = ((-b) + math.sqrt(o1)) / 2*a
y = ((-b) - math.sqrt(o1)) / 2*a
print("Value of x is: ",x,y)

# 5.	Write a Python program to swap two variables without temp variable?

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Numbers before swapping are - ",a, ",",b)

b = a+b
a = b-a
b = b-a

print("Numbers after swapping are - ",a, ",",b)
