a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
min_ = 0
max_ = 0
if a >= b and a >= c:
    max_ = a
    if b >= c:
        min_ = c
    elif c >= b:
        min_ = b
elif b >= a and b >= c:
    max_ = b
    if a >= c:
        min_ = c
    elif c >= a:
        min_ = a
elif c >= a and c >= b:
    max_ = c
    if b >= a:
        min_ = a
    elif a >= b:
        min_ = b
print(max_ - min_)
