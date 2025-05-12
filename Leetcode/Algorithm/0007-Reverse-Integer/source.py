# Name: 7. Reverse Integer
# URL:  https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            s = str(x)
            return int(s[::-1]) if int(s[::-1]) < 2**31 else 0
        elif x < 0:
            s = str(x)[1:]
            return -int(s[::-1]) if -int(s[::-1]) > -2**31 else 0
        else:
            return 0
