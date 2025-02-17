# Name: بلیت نهایی کدکاپ
# URL:  https://quera.org/problemset/245887

t = int(input())

for _ in range(t):
    result = False
    validate = {
        1:False,
        2:False,
        3:False,
        4:False,
        5:False,
        6:False,
    }
    n = list(map(int, input().split()))
    score_board_provincial = list(map(int, input().split()))
    count_accept_questions = list(map(int, input().split()))
    score_board_country = int(input())
    
    for index in range(6):
        if n[index] >= 7:
            validate[index+1] = True
            
        if (score_board_provincial[index] == 1) and (count_accept_questions[index] >= 2) and (validate[index+1] == True):
            validate[index+1] = True
            result = True
        
    if score_board_country <= 40 or result == True:
        print('YES')
    else:
        print('NO')

        
    