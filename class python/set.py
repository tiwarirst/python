#it is unorder collection. you can not access the element directly by indexing
#mutable
#no duplicate element
#not indexed
#support mathematical operation

#creating a set
myset={10,20,30,40,50}
print("set created using curly barces :",myset)

#creating a set using the set() constructor
anotherset=set([5,6,7,8,9,10])
print("set crated using set constructor:",anotherset)

#adding element to set
myset.add(6)
print("after adding the element :",myset)

#removing the element
myset.remove(30)
print("after removing element 30 :",myset)

#creating a set
fruits={"apple","banana","cherry"}
print(fruits)

#addding an element to set
fruits.add("orange")
print("after adding",fruits)

#checking memebership in a set

print("Is present in myset :",2 in myset)
print("length of myset :",len(myset))

# it is used when you want to remove the duplicate element from the list


#iterating over set
for element in myset:
    print(element)


#frozen set
# it is a immutable version of set. once created you cant add or remove element from the set

frozen_set=frozenset([1,2,3,4,5,6])
print("frozen set :",frozen_set)

# creating two set
citrus={"orange","lemon","lime"}
print(fruits.union(citrus))

#intersection of two set
print(fruits.intersection(citrus))

#difference of two set
print(fruits.difference(citrus))

#symmetric difference of two set

print(fruits.symmetric_difference(citrus))

#two different fxn 1.issubset,2.issuperset  it return the boolean  3.isdisjoint it have no common element

