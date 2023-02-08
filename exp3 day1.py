def is_happy(n):
    seen=set()
    while n not in seen:
        seen.add(n)
        n=sum(int(d)**2 for d in str(n))
    return n==1
x=int(input("x="))
print(is_happy(x))
