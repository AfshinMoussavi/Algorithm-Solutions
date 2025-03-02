# Name: شطرنج حرفه‌ای
# URL:  https://quera.org/problemset/2636


db = {
    '_1':1,
    '_2':1,
    '_3':2,
    '_4':2,
    '_5':2,
    '_6':8
}

inputs = list(map(int, input().split()))
result = []
for i in range(6):
    result.append(db[f'_{i+1}'] - inputs[i])

print(*result)

