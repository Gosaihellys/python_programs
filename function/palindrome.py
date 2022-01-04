def pali ():
    n=int(input("enter number"))
    k=n
    rev=0
    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        print("rev",rev)
        n=n//10
        print("n",n)
    if rev==k:
        g="palindrome num"
    else:
        g="not palidrome num"
    return g         
obj=pali()
print(obj)

