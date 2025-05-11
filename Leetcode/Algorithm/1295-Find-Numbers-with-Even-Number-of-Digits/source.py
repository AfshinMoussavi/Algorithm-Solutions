# Name: 1295. Find Numbers with Even Number of Digits
# URL:  https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for char in nums:
            if len(str(char)) % 2 == 0:
                count += 1
        return count