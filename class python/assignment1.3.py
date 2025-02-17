#You are a teacher and you have the scores of your students on a test.The scores are stored in a list.
#  Your task is to write a Python program to find the median score. If the number of scores is even,
#  the median is the average of the two middle scores.
# Scores of students
scores = [80, 90, 87, 96, 98, 56, 74, 34, 98, 23]
median = 0
scores.sort()
n = len(scores)
if n % 2 == 0:  
    median = (scores[n // 2 - 1] + scores[n // 2]) / 2
else:  
    median = scores[n // 2]
print("Sorted Scores:", scores)
print("Median:", median)
