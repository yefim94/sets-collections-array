# sets 
print("Create a new set:")
x = set()
print(x)
print(type(x))
print("\nCreate a non empty set:")
n = set([0, 1, 2, 3, 4])
print(n)
print(type(n))
print("\nUsing a literal:")
a = {1,2,3,'foo','bar'}
print(type(a))
print(a)
#collections
from collections import Counter
c = Counter(p=4, q=2, r=0, s=-2)
print(list(c.elements()))
#arrays
from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])