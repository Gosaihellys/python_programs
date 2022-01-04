def stu():
    n=int(input("how many students:"))
    name(n)
def name(n):
    i=1
    N=[]
    while i<=n:
        total=0
        name=input("enter name:")
        N.append(name)
        s=int(input("how many sub:"))
        subject(s)
        per(total,s)
        i=i+1
    return N    
def subject(s):
    i=1
    total=0
    while i<=s:
        m=int(input("enter marks:"))
        total=total+m
        per(total,s)
        i=i+1  
    return total
def per(total,s):
    p=total/s
    return p
obj=per(465,5)
print (obj)    



