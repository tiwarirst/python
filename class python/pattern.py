#simple pattern :print pattern of stars
rows=6
for i in range(1,rows+1):
    print("*"*i)
    print("")

# opposit pattern 
for i in range(1,rows+1):
    print("*"*((rows-i)+1))

#print reverse triangle of stars with space
print("")
for i in range(1,rows+1):
    print("_"*(i-1),"*"*((rows-i)+1))

#print square of numbers
print("")
for i in range(1,rows+1):
    print(str(i)*rows)

#print square of numbers 
print("")
count=1
for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(count," ", end="")
        count+=1
    print("")

#print hollow square
print("")
for i in range(1,rows+1):
    if(i==1 or i==rows):
        print("*"*rows)
    else:
        print("*"+"_"*(rows-2)+"*")
    
#print diamond
print("")
for i in range(1,rows+1):
    print(" "*(rows-i),"*"*(2*i-1))
for i in range(rows-2,-1,-1):
    print(" "*(rows-i-1)+"*"*(2*i+1))


# print half diamond of number
#               1
#             1   2

for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(str(j)+" ",end="")
    print()

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(''.join(str(k) for k in range(j,0,-1)),end='')
    print()

for i in range(1,rows+1):
    firsthalf=''.join(str(j) for j in range(1,i+1))
    secondhalf=''.join(str(j) for j in range(i-1,0,-1))
    print(firsthalf+secondhalf)
print()

