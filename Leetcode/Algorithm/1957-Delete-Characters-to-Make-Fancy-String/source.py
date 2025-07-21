# Name: 1957. Delete Characters to Make Fancy String
# URL:  https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        for index in range(len(s)-2):
                char = s[index]
                if s[index:index+3] != char*3 :
                        res += char

        res += s[len(s)-2:]
        return res

