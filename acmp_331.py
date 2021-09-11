n, m = input().split(":")
n = int(n)
m = int(m)

k, p = input().split()
k = int(k)
p = int(p)

print((n + k) % 24, m + p, sep=":")
