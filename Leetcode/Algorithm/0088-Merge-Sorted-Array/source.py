# Name: 88. Merge Sorted Array
# URL:  https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pointer1, pointer2 = m - 1, n - 1

        pointer = n + m - 1


        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[pointer] = nums1[pointer1]
                pointer1 -= 1
                pointer -= 1
            else:
                nums1[pointer] = nums2[pointer2]
                pointer2 -= 1
                pointer -= 1

        while pointer2 >= 0:
            nums1[pointer] = nums2[pointer2]
            pointer2 -= 1
            pointer -= 1

        print(nums1)














