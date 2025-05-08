# Name: 1768. Merge Strings Alternately
# URL:  https://leetcode.com/problems/merge-strings-alternately/description/

def mergeAlternately(word1: str, word2: str) -> str:
    maxLength = max(len(word1), len(word2))

    result = ""
    for index in range(maxLength):
        if index < len(word1):
            result += word1[index]
        if index < len(word2):
            result += word2[index]
    return result

