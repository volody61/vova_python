# s=['1', '45', '54', '5', '5', '6', '6', '6', '0']
# print(' '.join(s)[::-1])
a = int(input())
c = input().split()
s = list(map(int, c))
for i in range(len(s)-1, -1, -1):
    print(s[i], end=' ')
