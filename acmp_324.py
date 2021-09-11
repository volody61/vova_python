a = int(input())
b = a // 100
c = a % 100
d = (c % 10 * 10) + (c // 10)
if b == d:
    print("YES")
else:
    print("NO")
