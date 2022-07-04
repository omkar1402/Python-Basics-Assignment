# 1.	Write a Python program to find words which are greater than given length k?

n = int(input("Enter number of elements : "))
l = list(input("\nEnter the numbers(Comma separated) : ").split(','))[:n]
k = int(input("Enter length k: "))
 
lar = [] 
for e in l:
    if len(e)>k:
        lar.append(e)

print(lar)

# 2.	Write a Python program for removing i-th character from a string?

s = input("Enter string: ")
i = int(input("Enter ith position: "))
l = list()

for k in range(len(s)):
    l.append(s[k])
print(l)
for k in range(len(s)):
    if k==i:
        l.remove(l[k])

res = ''.join(l)
print(res)

# 3.	Write a Python program to split and join a string?

s = input("Enter string: ")
i = int(input("Enter ith position: "))
s = "Full stack data science"
l = s.split(' ')
print(l)

print(' '.join(l))


# # 4.	Write a Python to check if a given string is binary string or not?

s = input("Enter input: ")
c = 0

for i in range(len(s)):
    if s[i]=='0' or s[i]=='1':
        c = c+1
    
if c==len(s):
    print("Binary String")        
else:
    print("Not a binary string") 

# # 5.	Write a Python program to find uncommon words from two Strings?

s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

l1 = s1.split(' ')
l2 = s2.split(' ')
res = []
for a in l1:
    if a not in l2:
        res.append(a)

for a in l2:
    if a not in l1:
        res.append(a)

print("Uncommon words are: ",res)

# 6.	Write a Python to find all duplicate characters in string?

s = input("Enter string: ")
l = list(s)

print(l)

d = list()

for a in l:
    l.remove(a)
    if a in l:       
        d.append(a)

print(d)        

# 7.	Write a Python Program to check if a string contains any special character?

s = input("Enter String: ")
l = list(s)
# print(l)
s='[@_!#$%^&*()<>?/\|}{~:]='
sc = list(s)
# print(sc)
count = 0

for a in l:
    if a in s:
        count= count+1

if count>0:
    print("String contain special character")