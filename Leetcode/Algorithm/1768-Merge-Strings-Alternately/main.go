// Name: 1768. Merge Strings Alternately
// URL:  https://leetcode.com/problems/merge-strings-alternately/description/

package main

func mergeAlternately(word1 string, word2 string) string {
	maxLength := max(len(word1), len(word2))
	result := make([]byte, 0, maxLength*2)

	for i := 0; i < maxLength; i++ {
		if i < len(word1) {
			result = append(result, word1[i])
		}
		if i < len(word2) {
			result = append(result, word2[i])
		}
	}
	return string(result)
}


