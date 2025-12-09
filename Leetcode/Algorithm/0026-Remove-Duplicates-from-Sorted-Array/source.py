# Name: 26. Remove Duplicates from Sorted Array
# URL:  https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from operator import truediv


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1

        return i