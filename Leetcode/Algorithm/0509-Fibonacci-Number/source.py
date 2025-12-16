# Name: 509. Fibonacci Number
# URL:  https://leetcode.com/problems/fibonacci-number/description/


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        return self.fib(n-1) + self.fib(n-2)



