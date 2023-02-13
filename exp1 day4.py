x=int(input("enter a number"))
y=[]
for i in range (1,x+1):
    if i%5==0 and i%3==0:
        y.append("FIZZBUZZ")
    elif i%5==0:
        y.append("BUZZ")
    elif i%3==0:
        y.append("fizz")
    else:
        y.append(i)
print(y)
