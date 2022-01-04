# a=int(input("no:"))
# b=str(a)
# t=0
# for i in b:
#     d=int(i)**3
#     t=t+d
#     if a==t:
#         print("arm num:", t)
#     else:
#         print("not arm num:", t)    
# print(t)

def arm():
    a=int(input("no:"))
    b=str(a)
    t=0
    for i in b:
        d=int(i)**3
        t=t+d
        if a==t:
            r="arm num"
        else:
            r="not arm num"  
    return r
obj=arm()         
print(obj)