count=0
average=0
sum=0
heights=[160,178,168,163,170,171,162,192]
for i in heights :
    sum=(sum+i)
average=sum/len(heights)
for j in heights:
    if j>average:
        count=count+1
print("Averge Height:",average)
print("Height greater than average :",count)