# Name: دیوارهای شرکت
# URL:  https://quera.org/problemset/251441

def solve():
    n = int(input())
    l = [0] * n  # start
    r = [0] * n  # end

    for i in range(n):
        l[i], r[i] = map(int, input().split())

    ans = 2 * n
    for i in range(1, n):
        if r[i] <= l[i-1] or l[i] >= r[i-1]:
            ans += (r[i] - l[i]) + (r[i-1] - l[i-1])
        else :
            ans += abs(r[i] - r[i-1]) + abs(l[i] - l[i-1])

    ans += (r[0] - l[0]) + (r[n-1] - l[n-1])

    print(ans)
solve()

