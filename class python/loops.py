# loops
#range() generate immutable sequence of numbers 
x=range(6)
for i in x:
    print(i)

# parameterss in range 1.start(optional) ,2.stop(required) ,3.step(optional)
y=range(3,6)
for i in y:
    print(i)

z=range(3,20,2)
for i in z:
    print(i)

# looping and index and element
fruits=["apple","banana","cherry"]
for index,fruit in enumerate(fruits):
    print(f"index :{index} , fruit:{fruit}")

#nested for loop
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

#looping through the dictonary

person={"name":"rishu","age":20}
for key,value in person.items():
    print(f"{key}:{value}")