a, b = input().split()
a = int(a)
b = int(b)

c, d = input().split()
c = int(c)
d = int(d)

e, f = input().split()
e = int(e)
f = int(f)

g, h = input().split()
g = int(g)
h = int(h)

if a + c + e + g > b + d + f + h:
    print(1)
elif a + c + e + g < b + d + f + h:
    print(2)
else:
    print("DRAW")
