def task(ws):
    mi, ma = ws[0], ws[0]
    for w in ws:
        if w > ma:
            ma = w
        if w < mi:
            mi = w
    return (ma, mi)


input()
ws = list(map(int, input().split(" ")))
print(task(ws))
