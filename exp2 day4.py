x=int(input("enter total users"))
y=int(input("enter total staff users"))

if x==0 or y==0:
    print("invalid input")
else:
    a=y/3
    print("total users:",x-a-y)
