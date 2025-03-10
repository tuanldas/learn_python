equation = input().strip()

parts = equation.split()
a = int(parts[0])
b = int(parts[2])
c = int(parts[4])

# Kiểm tra phép toán
if a + b == c:
    print("YES")
else:
    print("NO")
