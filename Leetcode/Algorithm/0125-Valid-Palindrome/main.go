// Name: 125. Valid Palindrome
// URL:  https://leetcode.com/problems/valid-palindrome/description/

package main

import (
	"strings"
	"unicode"
)

func isPalindrome(s string) bool {
	cs := cleanString(s)
	for i := 0; i < len(cs)/2; i++ {
		if cs[i] != cs[len(cs)-1-i] {
			return false
		}
	}
	return true
}

func cleanString(s string) string {
	var builder strings.Builder
	for _, r := range s {
		if unicode.IsLetter(r) || unicode.IsDigit(r) {
			builder.WriteRune(unicode.ToLower(r))
		}
	}
	return builder.String()
}