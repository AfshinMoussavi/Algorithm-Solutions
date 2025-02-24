# Name: !بالین
# URL:  https://quera.org/problemset/175884

def calculate_floor(string:str):
    result = 0
    for char in string:
        if char == 'D':
            result -= 1
        else:
            result += 1
    return result