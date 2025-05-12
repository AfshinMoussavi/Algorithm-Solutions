// Name: 2094. Finding 3-Digit Even Numbers
// URL:  https://leetcode.com/problems/finding-3-digit-even-numbers/description/

package main

import (
	"sort"
)

func findEvenNumbers(digits []int) []int {
	n := len(digits)
	resultMap := make(map[int]bool)

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < n; k++ {
				if i != j && j != k && i != k {
					a, b, c := digits[i], digits[j], digits[k]
					if a == 0 {
						continue
					}
					if c%2 != 0 {
						continue
					}
					number := a*100 + b*10 + c
					resultMap[number] = true
				}
			}
		}
	}

	var result []int
	for number := range resultMap {
		result = append(result, number)
	}

	sort.Ints(result)
	return result
}
