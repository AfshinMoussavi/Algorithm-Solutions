# Name: شماره تلفن
# URL:  https://quera.org/problemset/291610


n = int(input())

for _ in range(n):
    phone = input()
    if len(phone) == 11 and phone.isdigit() and phone.startswith('09'):
        print(f"+98{phone[1:]}")
    elif len(phone) == 13 and phone[1:].isdigit() and phone.startswith('+') and phone[1:].startswith('98'):
        print(phone)
    elif len(phone) == 12 and phone.isdigit() and phone.startswith('98'):
        print(f"+{phone}")
    else:
        print('invalid')



