a=open('a.txt','r')
b=a.read()
v=b.split(' ')
print("word:",len(v))
e=[]
c=0
for i in b:
    c+=1
    

y=[]
for i in b:
    if i.isspace():
        y.append(i)
s=len(y)
z=c-s
print(z)




  