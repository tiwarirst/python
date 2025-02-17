#Problem statement:  you are working in a weather monitoring station.
#create a Python script to read temperature from the user and convert it from 
#Celsius to Fahrenheit or vice versa after that print weather is frizzing, cold, moderate, or hot.
def check(temp, unit):
    if unit == "f":
        if temp <= 32:
            print("Freezing")
        elif 33 <= temp <= 50:
            print("Cold")
        elif 51 <= temp <= 75:
            print("Moderate")
        else:
            print("Hot")
    elif unit == "c":
        if temp <= 0:
            print("Freezing")
        elif 1 <= temp <= 10:
            print("Cold")
        elif 11 <= temp <= 24:
            print("Moderate")
        else:
            print("Hot")

x=float(input("Enter the temperature :"))
print("1.celsius to fahrenheite \n 2.fahrenheite to celsius ")
c=int(input(" Enter your choice :"))
match c :
    case 1:
        y=(x*(9/5))+32
        print("Temperature :"+str(y)+chr(176)+"f")
        check(y,"f")
    case 2:
        y=((x-32)*(5/9))
        print("Temperature :"+str(y)+chr(176)+"c")
        check(y,"c")
    case default:
        print("------Enter the valid choice.----")
