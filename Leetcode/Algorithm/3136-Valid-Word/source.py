# Name: 3136. Valid Word
# URL:  https://leetcode.com/problems/valid-word/description/


class Solution:
    def isValid(self, word: str) -> bool:
        count_char = 0
        count_vowel = 0
        count_consonant = 0
        vowel = ['a', 'e', 'i', 'o', 'u']

        for char in word:
            if char.isalpha() == False and char.isdigit() == False:
                return False
            
            if char.isalpha() and char.lower() in vowel:
                count_vowel += 1
            elif char.isalpha() and char.lower() not in vowel:
                count_consonant += 1

            count_char += 1
        
        if count_char >=3 and count_consonant and count_vowel:
            return True
        return False