# Name: کافی‌نت رفقا
# URL:  https://quera.org/problemset/220668


count_computer, m = map(int, input().split())

computers = [0] * count_computer

for i in range(m):
    s, l = map(int, input().split())
    check = [0] * l
    s = s - 1
    flag = False
    for j in range(s,len(computers)):
        if computers[j:j+l] == check:
            flag = True
            computers[j:j+l] = [1] * l
            print(*computers, sep='')
            break
    if flag == False:
        print(*computers)

