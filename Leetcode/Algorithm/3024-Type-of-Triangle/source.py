# Name: 3024. Type of Triangle
# URL:  https://leetcode.com/problems/type-of-triangle/description/


class Solution:
    def triangleType(self, nums: list[int]) -> str:
        num_1 = nums[0]
        num_2 = nums[1]
        num_3 = nums[2]

        if num_1 + num_2 <= num_3 or num_1 + num_3 <= num_2 or num_2 + num_3 <= num_1:
            return "none"

        if num_1 == num_2 == num_3:
            return "equilateral"

        if num_1 == num_2 or num_2 == num_3 or num_3 == num_1:
            return "isosceles"

        return "scalene"