# 1. Write a Python program to find sum of elements in list?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
print(sum(l))

# 2. Write a Python program to Multiply all numbers in the list?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
mul=1

for i in range(len(l)):
    mul = mul*l[i]
print(mul)    

# 3. Write a Python program to find smallest number in a list?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
print(min(l))

# 4. Write a Python program to find largest number in a list?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
print(max(l))

# 5. Write a Python program to find second largest number in a list?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]

l.remove(max(l))
print(max(l))

# 6.	Write a Python program to find N largest elements from a list?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
m = int(input("Enter number pf largest elements you want: "))

l = sorted(l)
print(l[:m])

# 7.	Write a Python program to print even numbers in a list?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]

res = list()
for e in l:
    if e%2==0: res.append(e)

print(res)

# 8.	Write a Python program to print odd numbers in a List?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]

res = list()
for e in l:
    if e%2!=0: res.append(e)

print(res)

# 9.	Write a Python program to Remove empty List from List?

n = int(input("Enter number of elements : "))
l = list(input("\nEnter the numbers(Comma separated) : ").split(','))[:n]

print(type(l))
for e in l:
    if type(e)=='list':
        if len(e)==0:
            l=l.remove(e)

print(l)

# 10.	Write a Python program to Cloning or Copying a list?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]

res = l
print(res)

# 11.	Write a Python program to Count occurrences of an element in a list?

from collections import Counter
  
n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
x = int(input("Enter an element to count occurence: "))
  
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))