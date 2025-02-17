#you are alibrarian and you have a list of boook in your library.each book is reperesented as astring .
# #Your task is to write a python program to find out how many books in the libray you have a little longer 
# than 25 charcters.
books=['concept of physics by H C verma','software Engineering','Introduction to unix operating system','Design algorithm and analysis']
for i in range(len(books)):
    if(len(books[i])>25):
        print(books[i])
