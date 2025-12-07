# Name: ارزش سهام در روز
# URL:  https://quera.org/problemset/268834


n = int(input())
count = 0
for _ in range(n):
    text = input()
    if "rayancode" == text.lower():
        count += 1

print(count)


