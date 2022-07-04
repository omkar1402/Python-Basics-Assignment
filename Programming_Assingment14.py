# # Question 1:

# # Define a class with a generator which can iterate the numbers,
#  which are divisible by 7, between a given range 0 and n.

class div_generator:
    def __init__(self,in_num):
        self.in_num = in_num
    def get_numbers(self):
        for ele in range(0,self.in_num+1):
            if ele%7 == 0:
                yield ele
                
n = int(input("Enter a Number: "))
output = div_generator(n)
for ele in output.get_numbers():
    print(ele,end=' ')


# # Question 2:
# # Write a program to compute the frequency of the words from the input. 
# # The output should output after sorting the key alphanumerically. 

# # Suppose the following input is supplied to the program:

# # New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# # Then, the output should be:

# # 2:2

# # 3.:1

# # 3?:1

# # New:1

# # Python:5

# # Read:1

# # and:1

# # between:1

# # choosing:1

# # or:2

# # to:1

# # Solution:

s = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
l = s.split(" ")
print(l)
c=0 
d = {}

for i in range(len(l)):
    c = 0
    for j in range(len(l)):
        if l[i] == l[j]:
            c=c+1
        d[l[i]]   = c

for a in d:
    print(a, ": ", d[a])


# # Question 3:

# # Define a class Person and its two child classes: Male and Female.
# #  All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person:
    pass

class Male(Person):
    def getGender():
        return "Male"

class Female(Person):
    def getGender():
        return "Female"        

print(Male.getGender())
print(Female.getGender())


# # Question 4:
# #  write a program to generate all sentences where subject is in ["I", "You"]
# #  and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

sub = ["I", "You"]
verb = ["Play", "Love"]
obj = ["Hockey","Football"]
c = 0

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(sub[i],verb[j], obj[k])


# # Question 5:
# # Please write a program to compress and decompress the 
# # string "hello world!hello world!hello world!hello world!".

# # Solution : 

def compress(in_string):
    output = in_string[0]
    count = 1
    for ele in range(len(in_string)-1):
        if in_string[ele] == in_string[ele+1]:
            count +=1
        else:
            if count > 1:
                output += str(count)
            output += in_string[ele+1]
            count = 1
    if count > 1:
        output += str(count)            
    print(output)


def decompress(in_string):
    output = ''
    for ele in range(len(in_string)):
        if in_string[ele].isdigit():
            output += output[-1]*(int(in_string[ele])-1)
        else:
            output += in_string[ele]
    print(output)
    
        
compress("hello world!hello world!hello world!hello world!")
decompress("hel2o world!hel2o world!hel2o world!hel2o world!")


# # Question 6:
# # Please write a binary search function which searches an item in a sorted list. 
# # The function should return the index of element to be searched in the list.

sorted_list = [1,2,3,4,5,6,7,8,9,10]
def binary_search(in_list,in_num):
    low = 0
    high = len(in_list)-1
    while low <= high:
        mid = high+low//2
        if in_list[mid] < in_num:
            low = mid+1
        elif in_list[mid] > in_num:
            high = mid-1
        else:
            return mid+1
    else:
        return 'Invalid Input'
    
print(binary_search(sorted_list,8))
