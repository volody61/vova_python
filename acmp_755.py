a, b, n = input().split()
a = int(a)
b = int(b)
n = int(n)
if a + b >= n:
    print(a + b - n)
else:
    print("Impossible")