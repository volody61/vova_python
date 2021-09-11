# n, m, k = input().split()
# n = int(n)
# m = int(m)
# k = int(k)

n, m, k = map(int, input().split())
if (94 <= n <= 727 and
        94 <= m <= 727 and
        94 <= k <= 727):
    print(max(n, m, k))
else:
    print('Error')
#
# if n <= 727 and n >= 94:
#     if m <= 727 and m >= 94:
#         if k <= 727 and k >= 94:
#             # print(max(n, m, k))
#             if n >= m and n >= k:
#                 print(n)
#             elif m >= n and m >= k:
#                 print(m)
#             else:
#                 print(k)
#         else:
#             print("Error")
#     else:
#         print("Error")
# else:
#     print("Error")
