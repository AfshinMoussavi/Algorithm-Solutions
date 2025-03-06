# Name: سوال برنامه نویسی برنامه نویسی سوال
# URL:  https://quera.org/problemset/3408

n = int(input())
list_words = list(map(str, input().split()))
list_words = list_words[-1::-1]
print(*list_words)