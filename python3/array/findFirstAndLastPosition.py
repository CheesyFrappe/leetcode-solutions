"""
    34 - Find First and Last Position of Element in Sorted Array - Medium
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    Topics: Array
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        count = 0
        start = -1
        end = -1

        for i in range(len(nums)):
            if nums[i] == target:
                if count == 0:
                    start = i
                count += 1
        
        if count > 0:
            end = start + count - 1
        return [start, end]
        
