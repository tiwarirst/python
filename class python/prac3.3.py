# You are developing a weather monitoring system. Implement the following:
# ·        Collect temperature data for different cities.
# ·        Store each city’s data as a tuple containing its name and average temperature.
# ·        Display the temperature data for all cities.

print("-----------------Wheather monitoring system-----------------")
data={}
while True:
    key=input("Enter the city name (0 to exit .) :")
    if(key=="0"):
        break
    value=float(input("Enter the average temperature :"))
    data[key]=value
print(data)