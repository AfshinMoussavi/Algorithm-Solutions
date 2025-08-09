# Name: مُجَزا
# URL:  https://quera.org/problemset/129726

def separator(ls:list):
    even = []
    odd = []

    for number in ls:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return even, odd




