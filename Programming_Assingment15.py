# # Question 1:
# # Please write a program using generator to print the numbers which 
# # can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# # Example:
# # If the following n is given as input to the program:
# # 100
# # Then, the output of the program should be:
# # 0,35,70

# # Solution : 


n = int(input("Enter a number: "))

def divisible(n):
    for i in range(n):
        if (i%5==0) and (i%7==0):
            yield i

for e in divisible(n):
    print(e)



# # Question 2:
# # Please write a program using generator to print the even 
# # numbers between 0 and n in comma separated form while n is input by console.
# # Example:
# # If the following n is given as input to the program:
# # 10
# # Then, the output of the program should be:
# # 0,2,4,6,8,10

# # Solution :

n = int(input("Enter a number: "))

def even(n):
    for e in range(n):
        if e%2==0:
            yield e

for a in even(n):
    print(a)            


# # Question 3:
# # The Fibonacci Sequence is computed based on the following formula:
# # f(n)=0 if n=0
# # f(n)=1 if n=1
# # f(n)=f(n-1)+f(n-2) if n>1
# # Please write a program using list comprehension to print the Fibonacci 
# # Sequence in comma separated form with a given n input by console.
# # Example:
# # If the following n is given as input to the program:
# # 7

# # Then, the output of the program should be:
# # 0,1,1,2,3,5,8,13

# # Solution:

n = int(input("Enter a number: "))
a, b = 0,1
l = [0,1]

if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(n-1):
        l.append(a+b)
        a,b = b,a+b

print(l)         


# # Question 4:
# # Assuming that we have some email addresses in the "username@companyname.com" format,
# # please write program to print the user name of a given email address. 
# # Both user names and company names are composed of letters only.
# # Example:
# # If the following email address is given as input to the program:
# # john@google.com
# # Then, the output of the program should be:
# # john

id = input("Enter id: ")
print(id.split("@")[0])


# # Question 5:
# # Define a class named Shape and its subclass Square. 
# # The Square class has an init function which takes a length as argument. 
# # Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


class Shape():
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length*self.length)    

s = Square(20)
s.area()

spam = ['a', 'b', 'c', 'd'] 
print(spam[int(int('3' * 2) / 11)])