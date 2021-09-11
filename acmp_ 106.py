n = int(input())
b = 0
d = 0
while n > 0:
    c = int(input())
    if c == 0:
        b += 1
    else:
        d += 1
    n -= 1
if b < d:
    print(b)
else:
    print(d)
