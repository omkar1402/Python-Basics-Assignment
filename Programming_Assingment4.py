# Write a Python Program to Find the Factorial of a Number?

n = int(input("enter a number: "))
ans = 1
for i in range(1,n+1):
    ans = ans*i

print(ans)    


# Write a Python Program to Display the multiplication Table?

n = int(input("enter a number: "))
for i in range(1, 11):
    print(n*i)


# Write a Python Program to Print the Fibonacci sequence?

n = int(input("How many numbers you want in Fibonacci Series : "))
l = list()
a = 0
b = 1
for i in range(0, n):
    sum = a+b
    l.append(sum)
    a,b = b, sum
    print(a,b) 

print(l)


# Write a Python Program to Check Armstrong Number?

n = int(input("enter a number: "))
sum = 0
while(n>0):
    r = n%10
    sum = sum + r*r*r
    n = n//10

if sum == n :
    print("Number is an Armstrong Number")    
else:
    print("Number is not a Armstrong Number")    


# Write a Python Program to Find Armstrong Number in an Interval?

for i in range(2,500):
    sum = 0
    n = i
    while n>0:
        r = n%10
        sum = sum + r*r*r
        n = n//10

    if sum == i:
        print(i)    


# 6.	Write a Python Program to Find the Sum of Natural Numbers?

n = int(input("Enter a number: "))
sum = 0
for i in range(n+1):
    sum = sum + i

print(sum)