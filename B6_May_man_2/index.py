def check_yes_or_no(N):
    count, listN = 0, list(N)

    for i in listN:
        if (int(i) != 4) and (int(i) != 7):
            count += 1

    if count == 0:
        print('YES')
    else:
        print('NO')


testNumber = input().strip()

for i in range(int(testNumber)):
    N = input().strip()
    check_yes_or_no(N)
