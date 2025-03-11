import math

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def check_k_prime(test_cases):
    results = []
    for n in test_cases:
        k = euler_totient(n)
        results.append("YES" if is_prime(k) else "NO")
    return results


t = int(input())
cases = [int(input()) for _ in range(t)]

for res in check_k_prime(cases):
    print(res)
