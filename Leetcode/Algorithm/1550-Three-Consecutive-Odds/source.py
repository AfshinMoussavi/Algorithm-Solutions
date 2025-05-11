# Name: 1550. Three Consecutive Odds
# URL:  https://leetcode.com/problems/three-consecutive-odds/description/


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for index in range(len(arr)-2):
            if arr[index] % 2 == 1 and arr[index + 1] % 2 == 1 and arr[index + 2] % 2 == 1:
                return True
        return False