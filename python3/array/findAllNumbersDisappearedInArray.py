"""
    448 - Find All Numbers Disappeared in an Array - Easy
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
    Topics: Array
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        
        index = 0
        for i, num in enumerate(nums):
            if num > 0:
                nums[index] = i + 1
                index += 1
        
        return nums[:index]