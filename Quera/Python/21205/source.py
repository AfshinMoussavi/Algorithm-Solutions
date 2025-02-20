# Name: ثبت‌نام
# URL:  https://quera.org/problemset/21205


def check_registration_rules(**kwargs) -> list:
    result = []
    for username, password in kwargs.items():
        if username != "quera" and username != "codecup" and len(username) >= 4 and len(password) >= 6 and password.isdigit() == False:
            result.append(username)
    return result


