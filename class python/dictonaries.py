# unordered collection
#key-value pair'
#keys are unique
#keys are immutable
#values are mutable
#dynamic size
#accessing value by referring its key in square brace
#

#creating a dictonary
person={"name":"Rishu","age":20,"city":"kunda"}
print(person)

#creating another dict using dict()
another_dict=dict(name="rishu ",age=25,city='kunda')
print("another dictonary ",another_dict)

#accessing element 

print(person["name"])

# accessing vslues

print("name",another_dict["name"])

#accesssing values using get()

print("age",another_dict.get('age'))


# adding a new key value pair to the dictonary
person["profession"]='engineer'
print("After adding new key :",person)
person["age"]=21
print("After updating the value",person)

#removing key value pair

del another_dict["age"]
print("after deletion :",another_dict)


#checking if a key is in the dictonary
print("name" in person)
print("hobby" in person)

# getting keys

keys=another_dict.keys()
print("keys :",keys)

#getting values

print ("Values ",another_dict.values())

# getting value pair

print ("value pair :",another_dict.items())

#checking membership

print("is age a key in my dict ",'age'in another_dict)
print("is 30 value in my dict ","kunda" in another_dict.values())

#length of dictonary 
print("Length of dictonary:",len(another_dict))

#loop over anothe rdictt values
for val in another_dict.values():
    print (val)
    print("________________________________")
for key in another_dict.keys():
    print(key)
    print("________________________________")
for key,val in another_dict.items():
    print(key,val)
    print("________________________________")


# exercise

stateandcap={
    'gujrat':"gandhinagar",
    'maharashtra':'mumbai',
    'rajasthan':'jaipur',
    "bihar":'patna'
}
for key,val in stateandcap.items():
    print("the",key,"state has capital ->",val)




