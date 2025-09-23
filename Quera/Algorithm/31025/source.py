# Name: صبا و سوال ساده
# URL:  https://quera.org/problemset/31025

import math

n, k = map(int, input().split())

for _ in range(k):
    n = n / 2

print(math.floor(n))


