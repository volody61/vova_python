n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
if n + m > k and m + k > n and n + k > m:
    print("YES")
else:
    print("NO")
