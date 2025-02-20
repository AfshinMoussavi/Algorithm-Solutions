# Name: یافتن عدد اول
# URL:  https://quera.org/problemset/593

def is_prime(number:int):
    for digit in range(2,number):
        if number % digit == 0:
            return False
    return True

n = input()
b = sum(int(char) for char in n) 
n = int(n)
index = 1
while True:
    n += 1
    if is_prime(n) == True:
        if index == b:
            print(n)
            break
        index += 1
