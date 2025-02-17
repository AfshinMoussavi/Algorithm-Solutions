# Name: دیتاست
# URL:  https://quera.org/problemset/190993

binary_string_count, binary_input_count, binary_length = map(int, input().split(" "))

binary_db = {}

for _ in range(binary_string_count):
    binary_string, binary_type = map(str, input().split(' '))
    binary_db[binary_string] = binary_type


for _ in range(binary_input_count):
    binary_check = input()
    if binary_check in binary_db.keys():
        print(binary_db[binary_check])
    else:
        print('Unknown')    










