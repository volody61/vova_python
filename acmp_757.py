n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
c = n // 2
h = m // 6
o = k
if c <= h and c <= o:
    print(c)
elif h <= c and h <= o:
    print(h)
else:
    print(o)
