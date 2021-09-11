n, m, k, p = input().split()
n = int(n)
m = int(m)
k = int(k)
p = int(p)
if n >= p:
    print(p * m)
else:
    print(n * m + (p - n) * k)
