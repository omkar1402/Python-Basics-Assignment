# Write a Python Program to Find LCM?

a  = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(1, a*b+1):
    if i%a == 0 and i%b == 0:
        print("LCM is: ",i)
        break

# Write a Python Program to Find HCF?    

a  = int(input("Enter first number: "))
b = int(input("Enter second number: "))
l = list()
n = max(a,b)
for i in range(1, n+1):
    if a%i == 0 and b%i == 0:
        l.append(i)

print(max(l))        

# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

n = int(input("Enter a number: "))


print(bin(n).replace("0b", ""))
print(oct(n))
print(hex(n).replace("0x", ""))

# 4.	Write a Python Program To Find ASCII value of a character

s = input("Enter a character: ")

print(ord(s))

# 5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter Operation (+/-/*//) : ")

if c == '+':
    print("Sum is: ",a+b)
elif(c == '-'):
    print("Subtraction is: ",a-b)
elif(c == '*'):
    print("Multiplication is: ",a*b)     
elif(c == '/'):
    print("Division is: ",a/b)     
else:
    print("Enter a valid Operation")