# reduce fxn 
# take two arguents
#iterable sequence to be reduced
#initializer(optional)
from functools import reduce
number=[1,2,3,4,5]
sum_result=reduce(lambda x,y:x+y,number)
print(sum_result)


# reduce with using initialiser

sumr=reduce(lambda x,y:x+y,number,10)
print(sumr)

#Maximum element in a list
max=reduce(lambda x,y:x if x>y else y,number)
print(max)

# concatenate string in alist
string=["hello"," ","world"]
concatenate_dstring=reduce(lambda x,y:x+y,string)
print(concatenate_dstring)

# Factorial of number
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(5))


#removing duplicate from the list while preserving the order

mylist=[1,2,4,4,1,2,3,4,5]
unique=list(set(mylist))
unique.sort(key=lambda x:mylist.index(x))
print(unique)