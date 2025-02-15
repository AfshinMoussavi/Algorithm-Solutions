# Name: چاپ جمع
# URL:  https://quera.org/problemset/275795

x = int(input())
result=  ""
Sum = 0
for number in range(1,x+1):
    Sum += number
    if number == x:
        result += f"{number} = {Sum}"
    else:
        result += f"{number} + "
    
print(result)
