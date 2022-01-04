# stu=int(input("how many students:"))
# a=[]
# t=[]

# for i in range(stu):
#     name=input("student name:")
#     sub=int(input("how many subjects:"))
#     a.append(name)
#     total=0   
#     for j in range(sub):
#         marks=int(input("marks out of 100:"))
#         total=total+marks
#     t.append(total)
#     print("total",total)
# print(a)
# print(t)
a=[]
t=[]
m=[]
def stu():
    s=int(input("how many students:"))
    for i in range(s):
        name=input("student name:")
        sub=int(input("how many subjects:"))
        a.append(name) 
        total=0
        for j in range(sub):
            marks=int(input("marks out of 100:"))
            total=total+marks
            m.append(marks)
            t.append(total)
        return a

stu()

