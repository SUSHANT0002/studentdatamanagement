# ##################                                              whether the no is even or odd
# a = int(input('Enter a no.:-'))
# if (a % 2) == 0:
#     print(a,' is even')
# else:
#     print(a,' is odd')
# ###########################################                     simple intrest
# p = int(input('Enter principal amount:-'))
# r = int(input('Enter rate of intrest:-'))
# t = int(input('Enter time period in months:-'))
# SI = (p*r*t)/100
# print(SI)
#############################################                     fibonacci series
# n = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if n <= 0:
#    print("Please enter a positive integer")
# elif n == 1:
#    print("Fibonacci sequence upto",n,":")
#    print(n1)
# else:
#    print("Fibonacci sequence for ",n," terms:")
#    while count < n:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count =count+ 1
#################################################                number is prime or not
# n=int(input('Enter a integer:'))
# for i in range(2, n):
#     if (n % i) == 0:
#         print(n, 'is not a prime number')
#         break
# else:
#     print(n, 'is a prime number')
############################################# amstong no.   153=1*3 + 5*3 + 3*3=153
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
#
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
########################################   palindrome no.       141         525
# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")
# ###########################################      factorial of a number
# num =int(input("Enter a number:"))
# factorial = 1
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)
#
# ########################################           reverse a no.
# num = 1234
# reversed_num = 0
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
# print("Reversed Number: " + str(reversed_num))
#####################################, to find second max no.
# list1=[12,21,3,34,55,64,35]
# mx=max(list1[0],list1[1])
# secondmax=min(list1[0],list1[1])
# n=len(list1)
# for i in range(2,n):
#     if list1[i]>mx:
#         secondmax=mx
#         mx=list1[i]
#     elif list1[i]>secondmax and mx!=list1[i]:
#         secondmax=list1[i]
# print('second max number is',secondmax)
#




