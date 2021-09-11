# a = int(input())
#
# if a // (10 ** (len(str(a)) - 1)) - 1 == 1:
#     c = 0
#     while len(str(a)) > 0:
#         if a % 10 == 0:
#             print("NO")
#             c = 1
#             break
#         a = a // 10
#     if c == 0:
#         print("YES")
# else:
#     print("NO")
#

a = int(input())
c = 0
while len(str(a)) > 1:
    if a % 10 == 0:
        print("NO")
        c = 1
        break
    a = a // 10
if c == 0:
    print("YES")
