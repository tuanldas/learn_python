def calculator_years():
    n, x, m = map(float, input().split())

    current_money = n
    year = 0
    while current_money < m:
        current_money *= (1 + x / 100)
        year += 1

    print(year)


N = input().strip()
for _ in range(int(N)):
    calculator_years()
