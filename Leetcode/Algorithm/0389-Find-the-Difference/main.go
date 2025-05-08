// Name: 389. Find the Difference
// URL:  https://leetcode.com/problems/find-the-difference/description/

package main

import (
	"strings"
)

func findTheDifference(s string, t string) byte {
	for _, char := range s {
		if strings.ContainsRune(t, char) {
			t = strings.Replace(t, string(char), "", 1)
		}
	}
	return t[0] 
}
