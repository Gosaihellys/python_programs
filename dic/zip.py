a=[]
t=[]
student=int(input("how many students:"))
for i in range(student):
    name=input("student name:")
    sub=int(input("how many subjects:"))
    a.append(name)
    total=0   
    for j in range(sub):
        marks=int(input("marks out of 100:"))
        total=total+marks
    t.append(total)
    print("total",total)
print(a)
print(t)
z=dict(zip(a,t))
print(z)
