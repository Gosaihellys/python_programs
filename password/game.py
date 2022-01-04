import random
r=1
t=int(input("num of tournaments:"))
co=0
ur=0
for i in range(t):
    p=input("rock,paper,or scissors?")
    print("your choice is",p)
    a=["rock","paper","scissors"]
    c=(random.choice(a))
    print("computer's choice is",c)
    if p==c:
        print("match draw")
    elif(p=='rock'and c=='scissors') or (p=='paper'and c=='rock') or (p=='scissors'and c=='paper'):
        ur=ur+1
        print(ur)
        print("user win")
    else:
        co=co+1
        print(co)
        print("computer is win")
if co>ur:
    print("computer is winner")
else:
    print("user is winner")    

         
               
