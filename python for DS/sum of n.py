def sumof(n):
    if n==1:
        return 1
    else:
        return n+sumof(n-1)

n=int(input("enter the value of n:"))
print("the sum of:",sumof(n))