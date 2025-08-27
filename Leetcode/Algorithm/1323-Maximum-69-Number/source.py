# Name: 1323. Maximum 69 Number
# URL:  https://leetcode.com/problems/maximum-69-number/description/

class Solution:
    def maximum69Number(self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        return int(''.join(num))


