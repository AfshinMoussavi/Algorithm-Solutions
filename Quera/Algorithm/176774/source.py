# Name: جمع باستانی
# URL:  https://quera.org/problemset/176774

fingers = int(input())
hands = int(input())
number_1 = int(input())
number_2 = int(input())

total_fingers = fingers * hands
summation = number_1 + number_2

if summation % total_fingers == 0 and summation != 0:
    print(total_fingers)
else:
    print(summation % total_fingers)






