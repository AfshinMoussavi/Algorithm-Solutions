# Name: 125. Valid Palindrome
# URL:  https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
    

a = "1234"
b = "12345"

for i in range(len(a)//2):
    print(f"from first {a[i]} and from last {a[-i-1]}")

print("===")

for i in range(len(b)//2):
    print(f"from first {b[i]} and from last {b[-i-1]}")