# Name: 2259. Remove Digit From Number to Maximize Result
# URL:  https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        indexes = [i for i, c in enumerate(number) if c == digit]
        result = 0
        for index in indexes:    
            if int(number[:index] + number[index+1:]) > result:
                result = int(number[:index] + number[index+1:])

        return str(result)



