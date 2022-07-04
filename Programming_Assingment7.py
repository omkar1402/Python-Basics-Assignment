# Write a Python Program to find sum of array?


l = list(map(int(), input("Enter elements of list: ").split( )))
n = int(input())
l = map(int,input().split())

l = list(map(int, input("Enter elements: ")))[::-1]

l = list(l)
print(l[2])

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
# .strip().

print(l)
print("Sum of the list is: ",sum(l))

# 2. Write a Python Program to find largest element in an array?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]

print("Largest element in the array is: ",max(l))

# Write a Python Program for array rotation?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]

temp = l[-1]
res = list()
res.append(temp)

for i in range(1, len(l)):
    print(l[i])
    res.append(l[i])

res[0] = temp
print(res)   

# Write a Python Program to Split the array and add the first part to the end?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]

splitted1 = l[:len(l)//2]
splitted2 = l[len(l)//2:]

print("Splitted arrays are: ",splitted1, splitted2)

final = splitted2+splitted1
print(final)

# 5. Write a Python Program to check if given array is Monotonic?

n = int(input("Enter number of elements : "))
l = list(map(int,input("\nEnter the numbers(Comma separated) : ").split(',')))[:n]
c1, c2, c3 = 0, 0 , 0

for i in range(len(l)-1):
    print(l[i], l[i+1])
    if l[i] < l[i+1] and l[i+1] == max(l[:i+2]):
        c1 = c1+1
    elif(l[i] > l[i+1] and l[i+1]==min(l[:i+2])):
        c2 = c2+1
    else:  
        c3 = c3+1

if c1==len(l)-1 or c2 ==len(l)-1:
    print("Monotonic")
else:
    print("Non Monotonic")    
