# Name: 242. Valid Anagram
# URL:  https://leetcode.com/problems/valid-anagram/description/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)




