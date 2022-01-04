a=[1,2,3,4,5] 
b=[1,2,9,5,6]
o=[]
for i in range(len(a)):
    if a[i]==b[i]:
        o.append(a[i])
print(o)