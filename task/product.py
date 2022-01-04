a=10/100
b=20/100
c=30/100
choice=input("enter g or e or f :")
if choice=='g':
    total=0
    product=int(input("enter num of product:"))
    for i in range(product):
        price=int(input("enter price:")) 
        total=total+price
        g=(total*a)
        gst=total+g
    print("total:",total)
    print("product gst:",g)
    print("total gst:",gst)
elif choice=='e':    
    total=0
    product=int(input("enter num of product:"))
    for i in range(product):
        price=int(input("enter price:")) 
        total=total+price
        g=(total*b)
        gst=total+g
    print("total:",total)
    print("product gst:",g)
    print("total gst:",gst)
elif choice=='f':
    total=0
    product=int(input("enter num of product:"))
    for i in range(product):
        price=int(input("enter price:")) 
        total=total+price
        g=(total*c)
        gst=total+g
    print("total:",total)
    print("product gst:",g)
    print("total gst:",gst)
