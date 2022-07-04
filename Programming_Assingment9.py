# 1. Write a Python program to check if the given number is a Disarium Number?

n = int(input("Enter a number: "))
s = str(n)
temp = n
c = len(s)
c = int(c)
print(c)
sum = 0
while n>0:
    r = n%10
    sum = sum + r**c
    print(sum)
    n = n//10
    c = c-1

if sum == temp:
    print("Number is a Disarium Number ")
else:
    print("Number is not Disarium Number")    

# 2. Write a Python program to print all disarium numbers between 1 to 100?

res = []
for n in range(1,101):
    s = str(n)
    temp = n
    c = len(s)
    c = int(c)
    sum = 0
    while n>0:
        r = n%10
        sum = sum + r**c
        n = n//10
        c = c-1
    
    if sum == temp:
        res.append(sum)

print(res) 

# Write a Python program to check if the given number is Happy Number?

# n = int(input("Enter a number: "))
# sum = 0
# f_sum = [2222,1111]

# for i in range(1000):
#     if f_sum[-1]!=1 and f_sum[-2]>f_sum[-1]:
#         n = f_sum[-1]
#         sum = 0
#         while n>0:
#             r = n%10
#             sum = sum+r**2
#             n = n//10
#         f_sum.append(sum)
#         print(f_sum)
#     break        

# print(f_sum)    

def isHappyNumber(n):
    st=set()
    while (1):
        n = numSquareSum(n)
        if (n == 1):
            return True
        if n not in st:
            return False
        st.insert(n)

def numSquareSum(n):
    squareSum = 0;
    while(n):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum;
 
def isHappynumber(n):
    slow = n;
    fast = n;
    while(True):
        slow = numSquareSum(slow);
 
        fast = numSquareSum(numSquareSum(fast));
        if(slow != fast):
            continue;
        else:
            break;
 
    return (slow == 1)
 

n = int(input("Enter a number: "))
if (isHappynumber(n)):
    print(n , "is a Happy number")
else:
    print(n , "is not a Happy number")
 

# 5.	Write a Python program to determine whether the given number is a Harshad Number?

n = int(input("Enter a number: "))
temp = n
sum = 0

while n>0:
    r = n%10
    sum = sum + r
    n = n//10

if temp%sum ==0:
    print("Number is a Harshad Number")    
else:
    print("Number is not a Harshad Number")


# 6.	Write a Python program to print all pronic numbers between 1 and 100?

n = int(input("Enter a number: "))
l = list()
for i in range(1, (n//2)+1):
    if n%i==0:
        l.append(i)

print(l)

for i in range(len(l)):
    if l[i]*l[i-1] == n:
        print(l[i-1], l[i])
