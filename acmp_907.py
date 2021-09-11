n, a, b = input().split()
n = int(n)
a = int(a)
b = int(b) * 2
if n >= b and a >= b:
    print("YES")
else:
    print("NO")
