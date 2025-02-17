quote='good creator,worst destroyer'
print("Index of worst :",quote.find("worst"))
updated_quote=quote.replace("worst","best")
print(updated_quote)



#multiline string

poem="""
    roses are red,
    violets are ger.

hjhu
"""
print(poem)

#split

words=poem.split(" ")
print("split string :",words)


#whitespace stripping

my_string="     helllo world !        "
stripped_left=my_string.lstrip()
print(stripped_left)
stipped_right=my_string.rstrip()
print(stipped_right)

#finding substring
print(my_string.find("world"))
print(my_string.find("o",5))
print(my_string.count("l"))