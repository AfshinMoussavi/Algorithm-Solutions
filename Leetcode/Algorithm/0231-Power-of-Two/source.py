# Name: 231. Power of Two
# URL:  https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        number = 2
        while True:
            if n == 1 :
                return True
            if number > n:
                return False
            if number == n:
                return True
            number *= 2
