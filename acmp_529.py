n, m, k, p = input().split()
n = int(n)
m = int(m)
k = int(k)
p = int(p)
L = ((k - n) ** 2 + (p - m) ** 2) ** (1 / 2)
print(L)
