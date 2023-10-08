"""
    414 - Third Maximum Number - Easy
    https://leetcode.com/problems/third-maximum-number/
    topics = Array
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        if len(set(nums)) < 3:
            return max(set(nums))
        
        nums[:] = sorted(set(nums))
        
        return nums[-3]
