# Name: 389. Find the Difference
# URL:  https://leetcode.com/problems/find-the-difference/description/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in s:
            if char in t:
                t = t.replace(char, "", 1)
        return t