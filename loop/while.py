i=1
a=int(input("enter input:"))
total=0
while i<=a:
    price=int(input("enter number:"))
    total=total+price
    increment=total*0.1
    gst=total+increment
    i=i+1
print("total is ",total)
print("gst is",increment)
print("total with gst is",gst)