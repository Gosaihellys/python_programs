import random
a='123456789'
b='abcdefghijklmnop'
c='#$%^&*()@!'
while True:
    l=int(input("enter no:"))
    x=(random.sample(a,l))
    y=(random.sample(b,l))
    z=(random.sample(c,l))
    xyz=x+y+z
    random.shuffle(xyz)
    print("".join(xyz))
    if l==0:
     break



