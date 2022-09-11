############ password genrator 1
# import string as s
# from random import *
# hh = s.ascii_letters + s.digits +s.punctuation
# password = ''.join(choice(hh) for X in range(randint(5,5)))
# print(password)

############ password genrator 2
import random
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='1234567890'
symbol='/%^&*_+!@#$'
all=lower+upper+numbers+symbol
length=5
password="".join(random.sample(all,length))
print(password)