a=['a','b','c','d',1,2,3,4,5]

integer=[]
string=[]
for i in a:
    print(type(i))
    if type(i)==str:
        string.append(i)
    else:
        integer.append(i)


print("integer:",integer) 
print("string:",string)           