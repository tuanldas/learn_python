N = input().strip()

count, listN = 0, list(N)

for i in listN:
    if (int(i) == 4) or (int(i) == 7):
        count += 1

if count == 4 or count == 7:
    print('YES')
else:
    print('NO')
