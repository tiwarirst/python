# #creating fx
# def my_function():
#     print("Hello from fxn.")
# my_function()

# # passing parameter to fxn

# def fxn(fname):
#     print("fname",fname)
# fxn('rishu')
# fxn('hello')
# fxn('gh')
# # Arbitrary arguments
# # use d when unknown number of arguments
# def nfxn(*h):
#     print(h)
#     for i in h:
#         print(i)
# nfxn('rishu','shivam','aman')

# # keyword arguments
# #send argument with the key =value synntax .order does ot matter
# def hfxn(child3,child1,child2):
#     print("Youngest child :",child3)
# hfxn(child1="risshu",child2="anna",child3="chinmay")

# # default Parameter


# def kfxn( country='INDIA'):
#     print("I am from :",country)
# kfxn("brazil")
# kfxn("japan")
# kfxn("austria")

# #when you send list then it receive as list in fxn

# def frui(fruits):
#     for x in fruits:
#         print(x)
# fruits=["apple",'bana',"aam"]
# frui(fruits)

# # recursive fxn in python

# def fact(a):
#     if a==1:
#         return 1
#     else:
#         return a*fact(a-1)
# x=int(input("Enter the number"))
# print(fact(x))


# swap fxn

def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y
k=2
l=3
k,l=swap(k,l)
print(k)
print(l)




#----------------------------Lambda fxn----------------
#fxn with no name is called lambda fxn
#anonymous fxn
#created using lambda keyword 
# used for one line /sort fxn

#lambda arguments: expression

square =lambda x:x**2
print(square(5))


# map fxn


def newfxn(a):
    return len(a)
x=map(newfxn,('apple','banana','cherry'))
print(x)
print(list(x))

def chfxn(a,b):
    return a+b
o=map(chfxn,["rishu ","shivam ","amana "],["tiwari","thakur","tiwari"])
print(list(o))

#using lambda with map

numbers=[1,2,3,4,5]
squared_number=map(lambda x:x**2,numbers)
print(list(squared_number))


# lambda fxn ex

str1='Rishu tiwari'
upper1=lambda string:string.upper()
print(upper1(str1))

# cube
def cube(y):
    return y*y*y
lambda_cube=lambda y:y*y*y
print("using fxn value of cube :",cube(5))
print("using lambda fxn :",lambda_cube(5))


#

l=[1,5,2,4,3]
print("Sorted list :")
a=sorted(l)
print(a)
print("original list after sorting :")
print(l)
l.sort()
print(l)


# sorting alist of tuple by second element
data=[(3,10),(1,5),(2,80)]
sorted_data=sorted(data,key=lambda x:x[1])
print(sorted_data)

#recursion 

factorial=lambda n: 1 if n==1 else n*factorial(n-1)
print("factorial of 5:",factorial(5))

# length of variable in map
def myfxn(n):
    return len(n)
x=list(map(myfxn,("Rashtriya","raksha ","university")))
print(x)

# find fibbonacci using lambda fxn  imp for exam





# filter 

age=[5,3,18,3,43,78]
def myfxn(x):
    if x<18:
        return False
    else:
        return True
adults=filter(myfxn,age)
print(adults)
for x in adults:
    print(x)

# usnig lambda fxn filter even numbers

number=[2,5,3,4,8,7]
even_numbers=list(filter(lambda x: x%2==0,numbers))
print(even_numbers)