a, b, c, d, e, f = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)

if a >= b and a >= c:
    max1_ = a
    if b >= c:
        mid1_ = b
        min1_ = c
    else:
        mid1_ = c
        min1_ = b
elif b >= a and b >= c:
    max1_ = b
    if a >= c:
        mid1_ = a
        min1_ = c
    else:
        mid1_ = c
        min1_ = a
else:
    max1_ = c
    if b >= a:
        mid1_ = b
        min1_ = a
    else:
        mid1_ = a
        min1_ = b

if d >= e and a >= f:
    max2_ = d
    if e >= f:
        mid2_ = e
        min2_ = f
    else:
        mid2_ = f
        min2_ = e
elif e >= d and e >= f:
    max2_ = e
    if d >= f:
        mid2_ = d
        min2_ = f
    else:
        mid2_ = f
        min2_ = d
else:
    max2_ = f
    if d >= e:
        mid2_ = d
        min2_ = e
    else:
        mid2_ = e
        min2_ = d
print(max1_ * max2_ + mid1_ * mid2_ + min1_ * min2_)
