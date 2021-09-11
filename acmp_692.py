
n = int(input())
bin_lst = [2 ** i for i in range(15)]
# print(("YES" if n in bin_lst else "NO"))
# print(("YES" if int(input()) in [2 ** i for i in range(15)] else "NO"))



if n in bin_lst:
    print("YES")
else:
    print("NO")

# while n > 2:
#     n = n / 2
# if n == 2:
#     print('YES')
# else:
#     print('NO')