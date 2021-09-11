n, a, b = input().split()
n = int(n)
a = int(a)
b = int(b)
if n + a == b or b + a == n or n + b == a:
    print("YES")
else:
    print("NO")
