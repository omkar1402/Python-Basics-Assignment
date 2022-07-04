# # Question 1:

# # Write a program that calculates and prints the value according to the given formula:

# # Q = Square root of [(2 * C * D)/H]

# # Following are the fixed values of C and H:

# # C is 50. H is 30.

# # D is the variable whose values should be input to your program in a comma-separated sequence.

# # Example

# # Let us assume the following comma separated input sequence is given to the program:

# # 100,150,180

# # The output of the program should be:

# # 18,22,24

# # Solution
from cmath import sqrt


c = 50
h = 30
n = int(input("Enter number of elements : "))
d = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
print(d)
q = list()

for a in d:
    o1 = (2*c*a)/h
    o2 = sqrt(o1)
    print(type(o2))
    q.append(int(o2.real))

print(q)    


# # Question 2:
# # Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# # element value in the i-th row and j-th column of the array should be i*j.
# # Note: i=0,1.., X-1; j=0,1,¡Y-1.
# # Example
# # Suppose the following inputs are given to the program:
# # 3,5
# # Then, the output of the program should be:
# # [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


# Solution: 

import random
import numpy as np


i = int(input("Enter number of rows: "))
j = int(input("Enter number of columns: "))

# for a in range(i):
#     a = [random.randrange(0, i)  for b in range(j)]
# print(len(a))
# print(a)

m = np.random.rand(i,j)
print(m)


# # Question 3:
# # Write a program that accepts a comma separated sequence of words as input and prints the words in a 
# # comma-separated sequence after sorting them alphabetically.

# # Suppose the following input is supplied to the program:

# # without,hello,bag,world

# # Then, the output should be:

# # bag,hello,without,world

# # Solution: 

n = int(input("Enter number of elements : "))
d = input("\nEnter the numbers(Comma separated) : ").split(',')[:n]
print(d)
d = sorted(d)

s = []
for a in d:
    a = a.lower()
    s.append(a)
print(sorted(s))


# # Question 4:
# # Write a program that accepts a sequence of whitespace separated words as 
# # input and prints the words after removing all duplicate words and sorting them alphanumerically.

# # Suppose the following input is supplied to the program:

# # hello world and practice makes perfect and hello world again

# # Then, the output should be:

# # again and hello makes perfect practice world

# # Solution: 

s = input("Enter a string: ")
l = s.split(" ")
print(l)

for a in l:
    l.remove(a)
    if a in l:
        l. remove(a)

l = sorted(l)
print(l)        


# # Question 5:
# # Write a program that accepts a sentence and calculate the number of letters and digits.

# # Suppose the following input is supplied to the program:

# # hello world! 123

# # Then, the output should be:

# # LETTERS 10

# # DIGITS 3

# # Solution: 

s = input("Enter a string: ")
l = list(s)
print(l)

count = 0
for a in l:
    if a.isalpha():
        count = count+1
print("Leters ", count)

count = 0
for a in l:
    if a.isnumeric():
        count = count+1
print("Digits ",count)


# Question 6:
# A website requires the users to input username and password to register.
#  Write a program to check the validity of password input by users.

# Following are the criteria for checking the password:

# 1. At least 1 letter between [a-z]

# 2. At least 1 number between [0-9]

# 1. At least 1 letter between [A-Z]

# 3. At least 1 character from [$#@]

# 4. Minimum length of transaction password: 6

# 5. Maximum length of transaction password: 12

# Your program should accept a sequence of comma separated passwords and will 
# check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

# Example

# If the following passwords are given as input to the program:

# ABd1234@1,a F1#,2w3E*,2We3345

# Then, the output of the program should be:

# ABd1234@1

# Solution: 

l, u, p, d = 0, 0, 0, 0
inp = input("Enter passwords: ")
inp = inp.split(",")
output = []

for s in inp:
    if (len(s) >= 6 & len(s)<=12):
        for i in s:
    
            # counting lowercase alphabets
            if (i.islower()):
                l+=1           
    
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
    
            # counting digits
            if (i.isdigit()):
                d+=1           
    
            # counting the mentioned special characters
            if(i=='@'or i=='$' or i=='_'):
                p+=1          
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):        
        output.append(s)


print(output)        