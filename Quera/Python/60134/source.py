# Name: شطرنج میوه‌ای
# URL:  https://quera.org/problemset/60134


def fruits(tuple_of_fruits: tuple):
    result = dict()
    for item in tuple_of_fruits:
        if item["shape"] == "sphere" and 300 <= item["mass"] <= 600 and 100 <= item["volume"] <= 500:
            result[item["name"]] = result.get(item["name"], 0) + 1
    return result
