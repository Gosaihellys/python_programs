# a=int(input("enter number:"))
# if a==2 or a==3 or a==5 or a==7:
#     print("prime")
# elif a%2==0 or a%3==0 or a%7==0 or a%5==0:
#     print("not prime")
# else:
#     print("prime")

def prime(a):
    if a==2 or a==3 or a==5 or a==7:
        f="prime"
    elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
        f="not prime"
    else:
        f="prime" 
    return f
i=prime(2)
print(i)        
   
