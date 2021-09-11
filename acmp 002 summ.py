a = int(input())
b = 0
if a >= 1:
    for i in range(1, a + 1):
        b += i
else:
    for i in range(a, 2):
        b += i
print(b)
