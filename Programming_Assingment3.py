# 1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?

a = int(input("Enter a number: "))

if a==0:
    print("Entered number is Zero")
elif a>0:
    print("Entered numner is Positive")
else:
    print("Entered number is Negative")        


# 2.	Write a Python Program to Check if a Number is Odd or Even?

a = int(input("Enter a number: "))

if a%2 == 0:
    print("Entered number is Even Number")
else:
    print("Entered number is Odd Number")    


# # 3.	Write a Python Program to Check Leap Year?

y = int(input("Enter a year: "))

if(y<1000 or y>9999):
    print("Enter a valid year")
elif(y%4 == 0):
    print("Year is a leap year")
else:
    print("Year is not a leap year")    


# # 4.	Write a Python Program to Check Prime Number?

n = int(input("Enter a number: "))

if (n==0 or n==1):
    print("Number is not a Prime Number")
elif(n==2 or n==3 or n==5 or n==7):
    print("Number is a Prime Number")    
elif(n%2==0 or n%3==0 or n%5==0 or n%7==0):
    print("Number is not a Prime Number")
else:
    print("Number is Prime Number")


# 5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?    


for i in range(10000):
    if (i==0 or i==1):
        print("Number is not a Prime Number")
    elif(i==2 or i==3 or i==5 or i==7):
        print("Number is a Prime Number")    
    elif(i%2==0 or i%3==0 or i%5==0 or i%7==0):
        print("Number is not a Prime Number")
    else:
        print("Number is Prime Number")