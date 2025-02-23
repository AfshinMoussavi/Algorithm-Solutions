# Name: قورباغه‌ در چاه
# URL:  https://quera.org/problemset/235327

t = int(input())

for i in range(t):
    a,b, h = map(int, input().split())
    count = 0
    result = 0
    while True:
        if result >= h:
            print(count)
            break
        result += a
        count += 1
        if result >= h:
            print(count)
            break
        result -= b
        
        
    