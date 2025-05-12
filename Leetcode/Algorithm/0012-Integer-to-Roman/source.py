# Name: 12. Integer to Roman
# URL:  https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        result = ""

        for value in sorted(Roman.keys(), reverse=True):
            while num >= value:
                result += Roman[value]
                num -= value
        return result
