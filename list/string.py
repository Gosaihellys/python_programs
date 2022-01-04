a=['y','y','y','y','n','y','n','y']
count=0
e=[]
o=[]
for i in a:
    count=count+1
    if i=='y':
       e.append(i)
    elif i=='n':
         o.append(i)
print(len(o))
print(len(e))
 