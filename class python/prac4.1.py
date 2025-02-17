# Create a Python program to display the patterns
# USING FOR LOOP.

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

x=int(input("enter the number of lines :"))

# solution 1

for i in range(0,x):
    print(chr(65+i)*(x-i))

print()
#solution 2
count=1
for i in range(1,x+1):
    for j in range(0,i):
        print(count," ",end="")
        count+=1
    print()

print()
#solution 3
for i in range(1,x+1):
    for j in range(1,x+1):
        if i%2==0:
            if j%2==0:
              print("*",end="")
            else:
                print("-",end="")
        else:
            if j%2==0:
              print("-",end="")
            else:
                print("*",end="")
    print()
print()
#solution 4
for i in range(0,x):
    print(" "*(x-i)+"* "*(i+1))

print()
#solution 5
for i in range(1,x+1):
    for j in range(1,i+1):
        if i==1 or i==x :
            print("*",end='')
        else:
            if j==1 or j==i:
                print("*",end='')
            else:
                print(" ",end='')
    print()

print()
#solution 6
for i in range(1,x+1):
    if i%2==0:
        print(" "*(x-1)+"*")
    else:
        print("*"*x)

print()           
#solution 7
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end='')
    print()