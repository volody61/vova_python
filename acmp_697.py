n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
S = (m * k + n * k) * 2
B = S // 16
if S % 16 != 0:
    B += 1
print(B)
