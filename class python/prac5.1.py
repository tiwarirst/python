# #print all the pattern using while loop
# Create a Python program to display the patterns
# USING WHILE LOOP.

# 1. If input = 5 

# print 

# A A A A A 

# B B B B 

# C C C 

# D D 

# E

# 2.  If input = 5 

# print 

# 1 

# 2 3 

# 4 5 6 

# 7 8 9 10 

# 11 12 13 14 15

# 3. If input = 5 

# print 

# * - * - *

# - * - * -

# * - * - *

# - * - * -

# * - * - *

# 4.   If input = 5 

# print 

#     *

#    * *

#   * * *

#  * * * *

# * * * * *

# 5.  If input = 5 

# print 

# *

# * *

# *   *

# *      *

# * * * * *

# 6. If input = 5 

# print 

# * * * * *

#           *

# * * * * *

#           *

# * * * * * 

# 7.  If input = 5 

# print 

# 1

# 1 2

# 1 2 3

# 1 2 3 4

# 1 2 3 4 5


x=int(input("Enter the number of lines :"))
# solution 1
i=0
while x>0:
    print(chr(65+i)*x)
    x-=1
    i+=1

#solution 2

# count=1
# i=1
# while i<=x:
#     j=1
#     while j<=i:
#         print(count,' ',end='')
#         j+=1
#         count+=1
#     i+=1
#     print()

#solution 3

# i=1
# while i<=x:
#     j=1
#     while j<=x:
#         if i%2==0:
#             if j%2==0:
#                 print("*",end='')
#                 j+=1
#             else:
#                 print("-",end='')
#                 j+=1
#         else:
#             if j%2==0:
#                 print("-",end='')
#                 j+=1
#             else:
#                 print("*",end='')
#                 j+=1
#     i+=1
#     print()

#solution 4

# i=1
# while i<=x:
#     print(" "*(x-i)+"* "*i)
#     i+=1

#solution 5
# x=int(input("Enter the number of lines :"))
# i=1
# while i<=x:
#     j=1
#     while j<=i:
#         if i==1 or i==x:
#             print("*",end='')
#             j+=1
#         else:
#             if j==1 or j==i:
#                 print("*",end='')
#                 j+=1
#             else:
#                 print(" ",end='')
#                 j+=1
#     i+=1
#     print()

# # solution 6

# i=1
# while i<=x:
#     if i%2==0:
#         print(" "*(x-1)+"*")
#     else:
#         print("*"*x)
#     i+=1

# solution 7

# i=1
# while i<=x:
#     j=1
#     while j<=i:
#         print(j,' ',end='')
#         j+=1
#     i+=1
#     print()
