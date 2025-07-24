# Name: 14. Longest Common Prefix
# URL:  https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs, key=len)
        result = ""
        flag = False
        for index in range(len(strs[0])):
            char = strs[0][index]
            for word in strs:
                if word[index] != char:
                    flag = True
                    break

            if flag:
                break

            result += char

        return result

