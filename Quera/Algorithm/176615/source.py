# Name: اعداد شبه‌باینری
# URL:  https://quera.org/problemset/176775
import math



n = int(input())
res = 0
for i in range(1,n):
    if n % i == 0:
        res += i

if res == 0:
    print(0)
elif math.log2(res) % 1 == 0:
    print(1)
else:
    print(0)






