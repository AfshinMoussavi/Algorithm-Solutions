# Name: آخ جون طرف نیست!
# URL:  https://quera.org/problemset/3538

db = ['shanbe', '1shanbe', '2shanbe', '3shanbe', '4shanbe', '5shanbe', 'jome']

for _ in range(3):
    count = int(input())
    days = input().split()

    for j in range(len(days)):
        if days[j] in db:
            db.remove(days[j])

print(len(db))

