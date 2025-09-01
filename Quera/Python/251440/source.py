# Name: بی‌عملگر
# URL:  https://quera.org/problemset/251440


a, b, c = map(int, input().split("?"))

result = max(
    a*b*c,
    a+b+c,
    a+b*c,
    (a+b)*c,
    a*b+c,
    a*(b+c),
)
print(result)