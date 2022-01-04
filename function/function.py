def stu():
    s=int(input("enter how many students:")) 
    name(s)

def name(s):
    print(s)
    n=[]
    i=1
    while i<=s:
        name=input("enter name")
        j=int(input("enter subject"))
        n.append(name)
        subject(j)
        i=i+1
        return  n 
   

def subject(j):
    print(j)
    s=[]
    i=1
    while i<=j:
        s.append(subject)
        marks=int(input("marks out of 100:"))
        ma(marks)
        i=i+1
        return s
def ma(m): 
    print(m)
    g=[]
    i=1
    while i<=m:
        g.append(m)
        i=i+1
    print(g)
stu()


       





