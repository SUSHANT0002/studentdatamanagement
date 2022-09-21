
##############################                           reversing an array
# print('Array without reversing:-')
# n=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in n:
#     print(i,end='')
# print()
# print('Array after reversing:-')
# n=n[ : :-1]
# for i in n:
#     print(i,end='')

##################################### creating an array adding values  and searching values   in single dimensional array                     own
from array import *
val=array('i',[])
s=int(input('How many numbers you want to add in array: '))
for i in range(s):
    x=int(input('Enter the value:'))
    val.append(x)
print(val)

z=int(input('Enter the value you want to search:')) # one way to find value
l=0
for e in val:
    if z==e:
        print(l)
        break
    l += 1
print(val.index(z))                                 # 2nd way to find value

#########################################        multi dimensional array
