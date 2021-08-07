a = int(input())
b = 0
if a >= 0:
    while a >= 1:
        b += a
        a -= 1
else:
    while a <= 1:
        b += a
        a += 1
print(b)
