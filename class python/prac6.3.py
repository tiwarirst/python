# Temperature Converter:  You’re building a weather app. Create a Python program that converts temperatures between Celsius and Fahrenheit.
# •    Prompt the user to enter a temperature value and a unit (C or F).
# •    Calculate and display the converted temperature.
# •    Example: If the user enters 32 C, the program should output 89.6 F.

temp=float(input("Enter the temperature :"))
unit=input("Enter the temperature unit :")
if(unit=='c'):
    print("Converted temperature : {:.2f}".format((temp*(9/5))+32)+chr(176)+"F")
elif(unit=='f'):
    print("Converted temperature : {:.2f}".format((temp-32)*5/9)+chr(176)+"C")
else:
    print("-------------Invalid unit (Enter either c or f)------------")
