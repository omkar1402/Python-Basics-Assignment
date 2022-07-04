# Write a Python Program to Display Fibonacci Sequence Using Recursion?

n = int(input("Enter a number: "))

def Fibo(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    else:
        return(Fibo(n-1) + Fibo(n-2))

print(Fibo(n))

# 0 1 1 2 3 5

# 2.	Write a Python Program to Find Factorial of Number Using Recursion?

n = int(input("Enter a number: "))

def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return(n * fact(n-1))

print(fact(n))

# 3.	Write a Python Program to calculate your Body Mass Index?

# BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))

w = int(input("Enter Weight(in kg): "))
h = float(input("Enter height(in meter): "))

print("Yout BMI is: ", (w/(h*h)))

# 4.	Write a Python Program to calculate the natural logarithm of any number?

import math

n = int(input("Enter a number: "))
print("Logarithm is: ",math.log(n))

# 5.	Write a Python Program for cube sum of first n natural numbers?

n = int(input("Enter a number: "))
l = list()

for i in range(1, n+1):
    l.append(i*i*i)

print(l)    