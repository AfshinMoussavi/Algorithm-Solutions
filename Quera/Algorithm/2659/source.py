# Name: تست بینایی
# URL:  https://quera.org/problemset/2659


n = int(input())

correct = input()
check = input()
count = 0

for i in range(n):
    if correct[i] != check[i]:
        count += 1

print(count)





