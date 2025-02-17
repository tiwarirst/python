def fact(n):
    if n==1:return 0
    return n*fact(n-1)
def fibbo(n):
    sequence=[0,1]
    for i in range(2,n):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence
def is_prime(n):
    if n<=1:
        return False
    else:
        