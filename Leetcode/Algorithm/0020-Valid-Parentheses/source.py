# Name: 20. Valid Parentheses
# URL:  https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        Open = []

        for char in s:
            if char in "([{":
                Open.append(char)
            elif char in ")]}":
                if not Open:
                    return False
                last_open = Open.pop()
                if char == ")" and last_open != "(":
                    return False
                elif char == "]" and last_open != "[":
                    return False
                elif char == "}" and last_open != "{":
                    return False

        return len(Open) == 0 