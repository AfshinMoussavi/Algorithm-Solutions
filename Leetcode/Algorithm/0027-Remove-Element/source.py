# Name: 27. Remove Element
# URL:  https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[count] = nums[index]
                count += 1

        print(nums)
        return count



