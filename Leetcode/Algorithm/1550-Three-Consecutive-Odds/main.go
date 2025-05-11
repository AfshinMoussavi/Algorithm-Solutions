// Name: 1550. Three Consecutive Odds
// URL:  https://leetcode.com/problems/three-consecutive-odds/description/


package main

func threeConsecutiveOdds(arr []int) bool {
    for index := 0; index < len(arr)-2; index++ {
		if arr[index]%2 != 0 && arr[index+1]%2 != 0 && arr[index+2]%2 != 0 {
			return true
		}
	}
	return false
}