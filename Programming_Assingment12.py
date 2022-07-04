# 1.	Write a Python program to Extract Unique values dictionary values?

dict = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "k4": "v4"
}

l = dict.values()
l = list(l)
print(l)
o = list()

for a in l:
    l.remove(a)
    if a not in l:
        o.append(a)

print(o)        


# 2.	Write a Python program to find the sum of all items in a dictionary?

dict = {
    "k1": 50,
    "k2": 20,
    "k3": 33,
    "k4": 44
}

print(len(dict))

print(sum(dict.values()))


# 3.	Write a Python program to Merging two Dictionaries?

dict1 = {
    "k1": 50,
    "k2": 20
}

dict2 = {
    "k3": 33,
    "k4": 44
}

dict1.update(dict2)
print(dict1)


# # 4.	Write a Python program to convert key-values list to flat dictionary?

k = ['k1', 'k2', 'k3']
v = [1,2,3]

dict = {}

for i in range(len(k)):
        dict[k[i]]= v[i]

print(dict)


# 5.	Write a Python program to insertion at the beginning in OrderedDict?

from collections import OrderedDict

d = {'k1': 1, 'k2': 2, 'k3': 3}
print(d)

d = OrderedDict(d)
print(d)


# 6.	Write a Python program to check order of character in string using OrderedDict()?

from collections import OrderedDict

d = {'k1': 1, 'k4': 4,  'k2': 2, 'k3': 3}

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

d = OrderedDict(d)
print(d)
print(od)


# 7.	Write a Python program to sort Python Dictionaries by Key or Value?

d = {'k1': 1, 'k4': 4,  'k2': 2, 'k3': 3}
print(d)


dict1 = OrderedDict(sorted(dict.items(d)))
print(dict1)