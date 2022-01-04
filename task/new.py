a = int(input("enter value:"))
b = int(input("enter value:"))
choice = int(input("enter 1 for add, 2 for subs,3 for multi,4 for divison"))

if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice == 4:
    print(a/b)
else:
    print("not valid")                
