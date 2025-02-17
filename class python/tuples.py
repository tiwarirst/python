#tuples are immutable
#defined using parentheses ()
#contain element of different type like list
#used where data remains unchanged

#defining a tuple
my_tuple=('apple','banana','cherry')
print(my_tuple)

#accessing the element of tuple

print(my_tuple[0])
print(my_tuple[1])

#tuple slicing

print(my_tuple[1:3])

#negative indexxing

print(my_tuple[-1])
print(my_tuple[-2])

# if you want to moodifie then it give error

#you can create a tuple of any datatype or mixed datatype

number=(1,2,3,4,5,6,7,8,9,10)
print("first three element :",number[:3])
print("Element from index 2 to 5 :",number[2:6])
print("last three element :",number[-3])
print("every second element :",number[::2])
print("Reverse the tuple :",number[::-1])

#slice the tuple to get first and second half

first_Half=number[:len(number)//2]
second_half=number[len(number)//2:]
print(f"first half {first_Half}")
print(f"second half :{second_half}")


# sorting for this first convert it into list then convert back into the tuple

first_Half=list(first_Half)
second_half=list(second_half)
first_Half.sort()
second_half.sort(reverse=True)
print(f"first half {tuple(first_Half)}")
print(f"first half {tuple(second_half)}")