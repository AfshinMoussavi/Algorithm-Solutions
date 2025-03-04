# Name: صدگان خسته
# URL:  https://quera.org/problemset/3406

string_1 = list((input()))
string_2 = list((input()))

number_1 = ''
for i in range(2,-1,-1):
    number_1 += string_1[i]
number_1 = int(number_1)

number_2 = ''
for i in range(2,-1,-1):
    number_2 += string_2[i]
number_2 = int(number_2)


if number_1 < number_2:
    print(*string_1, sep='', end='')
    print(' < ', end='')
    print(*string_2, sep='', end='')
    
    
elif number_2 < number_1:
    print(*string_2, sep='', end='')
    print(' < ', end='')
    print(*string_1, sep='', end='')
else:
    print(*string_1, sep='', end='')
    print(' = ', end='')
    print(*string_2, sep='', end='')
