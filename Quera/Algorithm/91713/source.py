# Name: شماره رند
# URL:  https://quera.org/problemset/91713

def validation(number:str):
    if number == number[::-1]:
        return "Ronde!"

    db = {}
    for i in range(len(number)):
        char = number[i]

        if number[i:i+3] == char*3:
            return "Ronde!"

        if char in db.keys():
            db[char] += 1
        else:
            db[char] = 1

        if db[char] == 4:
            return "Ronde!"

    return "Rond Nist"


t = int(input())
for _ in range(t):
    phone = input()
    print(validation(phone))




