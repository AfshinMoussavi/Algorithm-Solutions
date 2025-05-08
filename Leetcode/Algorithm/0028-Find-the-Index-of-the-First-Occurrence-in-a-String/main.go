// Name: 28. Find the Index of the First Occurrence in a String
// URL:  https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

package main

import (
	"strings"
)

func strStr(haystack string, needle string) int {
	return strings.Index(haystack, needle)

}