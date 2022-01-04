a=int(input("enter number:"))
total=0
for i in range(a):
    price=int(input("enter number:"))
    total=total+price
    increment=total*0.1
    gst=increment+total
    print("price is",total)
    print("increment is",increment)
    print("gst is",gst)    

