a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

if a <= b <= c:
    print(a, b, c)
elif b <= c <= a:
    print(b, c, a)
elif b <= a <= c:
    print(b, a, c)
elif c <= a <= b:
    print(c, a, b)
elif c <= b <= a:
    print(c, b, a)
else:
    print(a, c, b)
