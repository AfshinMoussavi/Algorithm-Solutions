# Name: تَخَطّی‌گَری
# URL:  https://quera.org/problemset/129728


print(*sorted([char if (ord(char) - 97) % 2 == 0  else char.upper()  for char in input()], reverse=True))

