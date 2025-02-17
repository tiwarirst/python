#defining a list
my_list=['apple','banana','cherry']
print(my_list)

#accessing elemnets in a list

print(my_list[0])
print(my_list[1])

# list slicing
print(my_list[1:3])

#negative indexing

print(my_list[-1])
print(my_list[-2])

#Modifying element

my_list[1]='Blueberry'
print(my_list[1])

#defining a list of integer

number=[1,2,4,5,6,7,9]
print("List of numbers :",number)

#Define a list of strings

fruits=['apple','banana','orange','kiwi']
print("list of fruits :",fruits)

#defin a list of mix type

mix_list=[1,'list',True,3.14]
print("Mixed List: ",mix_list)

#slicing the list to get the potion of list

print("First three elements of list:",number[:3])
print("Every second element : ",number[::2]) #every 3rd element
print("REversed list :",number[::-1])

#define a list of lists (nested list)
nested_list=[[1,2,3],[4,5,6],[7,8,9]]   #It is just like nested array
print("nested list:",nested_list)

#define an empty list
empty_list=[]
print("Empty List:",empty_list)

#operations on list:-
#reverse list
number.reverse()
print(F"list after reverse :{number}")

#slice the list to get first half and second half
first_half=number[:len(number)//2]
second_half=number[len(number)//2:]
print(f"first half:{first_half}")
print(f"Second Half:{second_half}")


#sort the first half in ascending order and second half in descending order

first_half.sort()
second_half.sort(reverse=True)
print(f"First sorted half:{first_half}")
print(f"Second half sorted in descendin order: {second_half}")

#merge the two halves of the list

final_list=first_half+second_half
print(f"Final list:{final_list}")

#create nested list

school=[
    ["shivam","Rishu","Lav"],  #class 1
    ["aman","vicky","shiva"],  #class 2
    ["madhav","gaurav","ankit"]  #class 3
]

#accessing the element of nested list
print("the whole school",school)

#acccessing each class
for i in range(len(school)):
    print("class",i+1,": ",school[i])

#Accesssing each student

for i in range(len(school)):
    for j in range(len(school[i])):
        print("student",j+1,"in class",i+1,": ",school[i][j])


# enuumerate fxn used for any iterative datatype itt adds counter to each and every eleelement 
x=['x','y','z']
y=enumerate(x)
print(list(y))


# using a custom index

a=["Rashtriya","Raksha","University"]
print(a)

for index,x in enumerate(a,start=1):
    print(index,x)

#Define a nested list containing some data
nested_list=[
    [1,2,3],
    ['a','b','c'],
    [True,False,True]
]

#iterate over each sublist

for sublist_index,sublist in enumerate(nested_list):
    print(f"Sublist {sublist_index}:")
    #iterate over each element in list
    for element_index,element in enumerate(sublist):
        print(f" Element {element_index}: {element}")
