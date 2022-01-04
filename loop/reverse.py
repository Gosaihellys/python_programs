
a=int(input("enter numbers"))
k=a
rev=0
while a>0:
    r=a%10
    print(r)
    rev=(rev*10)+r
    a=a//10
if rev==k:
    print("palindrome")
else :
    print("not palidrome")        
print(rev)


     
      

