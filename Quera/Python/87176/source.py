# Name: بازی تفاضل
# URL:  https://quera.org/problemset/87176

def game(number):
	digit_1, digit_2 = str(number)
	digit_1 = int(digit_1)
	digit_2 = int(digit_2)
	return (max(digit_2, digit_1) - min(digit_1, digit_2))
