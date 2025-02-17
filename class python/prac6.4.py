# Vowel Counter:  You’re developing a text analysis tool. Write a Python program that reads a sentence from the user.
# •    Count the number of vowels (a, e, i, o, u) in the sentence.
# •    Display the total count of each vowel.
import re
result={}
sentence=input("Enter the sentence : ")
print("\nRasult after text analysis : ",end=' ')
count = len(re.findall('a', sentence))
result['a']=count
count=0
count = len(re.findall('e', sentence))
result['e']=count
count=0
count = len(re.findall('i', sentence))
result['i']=count
count=0
count = len(re.findall('o', sentence))
result['o']=count
count=0
count = len(re.findall('u', sentence))
result['u']=count
print(result)
