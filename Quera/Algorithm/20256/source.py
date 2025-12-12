# Name: رژیم سخت
# URL:  https://quera.org/problemset/20256

s = input()

red = 0
yellow = 0
green = 0

for char in s:
    if char == 'R':
        red += 1
    elif char == 'Y':
        yellow += 1
    else:
        green += 1

if (red >= 3) or (red >= 2 and yellow >= 2) or (green == 0):
    print('nakhor lite')

else:
    print('rahat baash')




