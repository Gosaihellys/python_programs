stu=int(input("how many stu:"))
i=1
total=0
while i<=stu:
    name=input("enter name:")
    sub=int(input("num of subjects:"))
    i=i+1
    j=1
    while j<=sub:
        marks=int(input("mark out of 100:"))
        j=j+1
        
        total=total+marks
        ave=total/300
    print("num of total:",total)
    print("enter ave:",ave)
        



       