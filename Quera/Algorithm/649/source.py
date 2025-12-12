# Name: اول‌بینی
# URL:  https://quera.org/problemset/649

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True


a = int(input())
b = int(input())

first = True
for i in range(a+1, b):
    if is_prime(i):
        if not first:
            print(",", end="")
        print(i, end="")
        first = False
