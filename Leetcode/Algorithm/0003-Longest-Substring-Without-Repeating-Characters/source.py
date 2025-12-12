# Name: 3. Longest Substring Without Repeating Characters
# URL:  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for index in range(len(s)):
            items = []
            for j in range(index, len(s)):
                if ord(s[j]) not in items:
                    items.append(ord(s[j]))
                else:
                    break
            ans = max(ans, len(items))
        return ans

