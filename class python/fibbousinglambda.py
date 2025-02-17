
fibbonacci=lambda n: n if n==0 or n==1 else fibbonacci(n-1)+fibbonacci(n-2)
n=int(input("Enter the number of terms"))
for i in range(n):
   print(fibbonacci(i))