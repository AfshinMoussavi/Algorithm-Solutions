# Name: رشته فیبوناچی
# URL:  https://quera.org/problemset/17675


fibonacci = [1, 2]
for i in range(10):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])


n = int(input())

ans = ""
for i in range(1, n+1):
    if i in fibonacci:
        ans += "+"
    else:
        ans += "-"

print(ans)
