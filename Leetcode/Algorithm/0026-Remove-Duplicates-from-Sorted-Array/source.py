# Name: 26. Remove Duplicates from Sorted Array
# URL:  https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from operator import truediv


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        unique = []
        i = 0
        while i < len(nums):
            if nums[i] in unique:
                nums.pop(i)
            else:
                unique.append(nums[i])
                i += 1
        return len(unique)






