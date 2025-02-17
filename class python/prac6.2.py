# Student Grade Analyzer: 
#  As a teacher, you have a list of student names and scores (out of 100) for a test.
# •    Write a Python program that calculates the average score and identifies 
# students who scored above the average.
result={}
while True:
    key=input("Enter the name of student(-1 when data entry is complete) :")
    if key=='-1':
        break
    value=int(input("Enter the marks :"))
    result[key]=value
sum=0
for x in result.values():
    sum+=x
average=sum/len(result)
print("\n Student whose marks is above average :",end=' ')
for key,value in result.items():
    if value>average:
        print(key+" ")

