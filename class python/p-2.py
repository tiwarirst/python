# # date : 9/01/25
# prgrm to demonstrate the string concatenation
s1="jai"
s2="shree"
s3="Ram"
concate_str=s1+" "+s2+" "+s3
print(concate_str)

#program to concate and repeat string
s="Radhe"+" "+"radhe"
t="radhe"*6
print(s)
print(t)

#prgrm to find string length
st1="Radhe Radhe"
print("Length of the string is :",len(st1))

#prgram to demonstrate string indexing
str1="Mahakal"
print("First character :",str1[0])
print("last character :",str1[-2])

#string slicing

stri1="Radhe Radhe"
print("First five character :",stri1[2:7:3])
print("last five character :",stri1[-5:])

#string formATTING
name="Rishu "
age=20
height=1.2
formatted_string="My name is {},I'm {}years old and my height is {:.3f} feet".format(name,age,height)
print(formatted_string)

# string methodas and properties
w="My name is Rishu Tiwari."
print(w.upper())
print(w.lower())
print(w.replace("a","Another"))
print(w.split())
print(w.startswith("This"))
print(w.endswith("The end.."))
print(w.find("is"))
print(w.count("is"))
print(len(w))
print(w.title())
print(w.isalpha())
print(w.isdigit())
print(w.isspace())